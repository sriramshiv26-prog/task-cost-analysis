#!/bin/bash
#
# Ollama Installation & Model Setup Script
# Detects OS and hardware, installs Ollama, pulls recommended models
# Tested on: Mac M1 Max, Mac Intel, Windows RTX 5060 Ti, Linux
#
# Usage: bash setup/ollama-installation.sh
#

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}===============================================${NC}"
echo -e "${GREEN}Ollama Installation & Model Setup${NC}"
echo -e "${GREEN}Task Cost Analysis Framework${NC}"
echo -e "${GREEN}===============================================${NC}\n"

# Detect OS
OS_TYPE="unknown"
if [[ "$OSTYPE" == "darwin"* ]]; then
    OS_TYPE="macos"
    echo -e "${YELLOW}Detected: macOS${NC}"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    OS_TYPE="linux"
    echo -e "${YELLOW}Detected: Linux${NC}"
elif [[ "$OSTYPE" == "msys" ]] || [[ "$OSTYPE" == "win32" ]]; then
    OS_TYPE="windows"
    echo -e "${YELLOW}Detected: Windows${NC}"
else
    echo -e "${RED}Unsupported OS: $OSTYPE${NC}"
    exit 1
fi

# Detect hardware
echo -e "\n${YELLOW}Detecting hardware...${NC}"
HARDWARE="unknown"
VRAM=0

if [[ "$OS_TYPE" == "macos" ]]; then
    # Check for Apple Silicon (M1/M2/M3)
    if sysctl -n sysctl.proc_translated &>/dev/null; then
        HARDWARE="apple_silicon"
        RAM=$(system_profiler SPHardwareDataType | grep "Memory:" | awk '{print $2}')
        echo -e "${GREEN}✓ Apple Silicon detected (${RAM})${NC}"
    else
        HARDWARE="mac_intel"
        RAM=$(system_profiler SPHardwareDataType | grep "Memory:" | awk '{print $2}')
        echo -e "${GREEN}✓ Mac Intel detected (${RAM})${NC}"
    fi
elif [[ "$OS_TYPE" == "linux" ]]; then
    # Check for NVIDIA GPU
    if command -v nvidia-smi &> /dev/null; then
        HARDWARE="linux_nvidia"
        VRAM=$(nvidia-smi --query-gpu=memory.total --format=csv,noheader | awk '{print $1}')
        echo -e "${GREEN}✓ Linux with NVIDIA GPU detected (${VRAM}MB)${NC}"
    else
        HARDWARE="linux_cpu"
        RAM=$(free -h | awk 'NR==2 {print $2}')
        echo -e "${GREEN}✓ Linux CPU-only detected (${RAM})${NC}"
    fi
elif [[ "$OS_TYPE" == "windows" ]]; then
    # Check for NVIDIA GPU
    if command -v nvidia-smi &> /dev/null; then
        HARDWARE="windows_nvidia"
        VRAM=$(nvidia-smi --query-gpu=memory.total --format=csv,noheader | head -1 | awk '{print $1}')
        echo -e "${GREEN}✓ Windows with NVIDIA GPU detected (${VRAM}MB)${NC}"
    else
        HARDWARE="windows_cpu"
        echo -e "${YELLOW}⚠ Windows CPU-only detected${NC}"
    fi
fi

# Step 1: Install Ollama
echo -e "\n${YELLOW}Step 1: Installing Ollama...${NC}"

if command -v ollama &> /dev/null; then
    echo -e "${GREEN}✓ Ollama already installed${NC}"
    OLLAMA_VERSION=$(ollama --version 2>/dev/null || echo "unknown")
    echo -e "  Version: $OLLAMA_VERSION"
else
    echo -e "${YELLOW}  Downloading Ollama...${NC}"
    if [[ "$OS_TYPE" == "macos" ]]; then
        curl -fsSL https://ollama.ai/install.sh | sh
        echo -e "${GREEN}✓ Ollama installed on macOS${NC}"
    elif [[ "$OS_TYPE" == "linux" ]]; then
        curl -fsSL https://ollama.ai/install.sh | sh
        echo -e "${GREEN}✓ Ollama installed on Linux${NC}"
    elif [[ "$OS_TYPE" == "windows" ]]; then
        echo -e "${YELLOW}  Please download from https://ollama.ai and run the installer${NC}"
        echo -e "${YELLOW}  Then re-run this script${NC}"
        exit 1
    fi
fi

# Step 2: Start Ollama daemon
echo -e "\n${YELLOW}Step 2: Starting Ollama daemon...${NC}"

if [[ "$OS_TYPE" == "macos" ]]; then
    # Check if Ollama daemon is running
    if pgrep -x "ollama" > /dev/null; then
        echo -e "${GREEN}✓ Ollama daemon already running${NC}"
    else
        echo -e "${YELLOW}  Starting Ollama daemon...${NC}"
        launchctl start com.ollama.ollama 2>/dev/null || {
            echo -e "${RED}  Could not start Ollama daemon${NC}"
            echo -e "${YELLOW}  Manual start: launchctl start com.ollama.ollama${NC}"
        }
        sleep 3
        if pgrep -x "ollama" > /dev/null; then
            echo -e "${GREEN}✓ Ollama daemon running${NC}"
        else
            echo -e "${RED}✗ Failed to start Ollama daemon${NC}"
            exit 1
        fi
    fi
elif [[ "$OS_TYPE" == "linux" ]]; then
    # Check if systemd service is running
    if systemctl is-active --quiet ollama; then
        echo -e "${GREEN}✓ Ollama systemd service running${NC}"
    else
        echo -e "${YELLOW}  Starting Ollama service...${NC}"
        systemctl start ollama 2>/dev/null || {
            echo -e "${RED}  Could not start Ollama service${NC}"
            echo -e "${YELLOW}  Manual start: systemctl start ollama${NC}"
        }
        sleep 3
        if systemctl is-active --quiet ollama; then
            echo -e "${GREEN}✓ Ollama systemd service running${NC}"
        fi
    fi
fi

# Step 3: Pull models based on hardware
echo -e "\n${YELLOW}Step 3: Pulling recommended models...${NC}"

# Test Ollama connection
echo -e "  Testing Ollama connection..."
if ! curl -s http://localhost:11434/api/tags > /dev/null 2>&1; then
    echo -e "${RED}✗ Could not connect to Ollama daemon at localhost:11434${NC}"
    echo -e "${YELLOW}  Make sure Ollama daemon is running${NC}"
    exit 1
fi
echo -e "${GREEN}✓ Connected to Ollama${NC}"

# Model configuration by hardware
declare -a MODELS_TO_PULL

if [[ "$HARDWARE" == "apple_silicon" ]]; then
    echo -e "\n${YELLOW}Recommended for Apple Silicon (M1/M2/M3 Max):${NC}"
    MODELS_TO_PULL=(
        "qwen2.5-coder:1.5b"
        "qwen2.5-coder:7b"
        "mistral:latest"
        "gemma4:latest"
        "llava:latest"
        "deepseek-r1:1.5b"
    )
elif [[ "$HARDWARE" == "mac_intel" ]]; then
    echo -e "\n${YELLOW}Recommended for Mac Intel (limited VRAM):${NC}"
    MODELS_TO_PULL=(
        "qwen2.5-coder:1.5b"
        "mistral:latest"
        "gemma4:latest"
    )
elif [[ "$HARDWARE" == "windows_nvidia" ]] || [[ "$HARDWARE" == "linux_nvidia" ]]; then
    echo -e "\n${YELLOW}Recommended for NVIDIA GPU (RTX 5060 Ti / A100):${NC}"
    MODELS_TO_PULL=(
        "qwen2.5-coder:1.5b"
        "qwen2.5-coder:7b"
        "mistral:latest"
        "deepseek-r1:1.5b"
    )
else
    echo -e "\n${YELLOW}Recommended for CPU-only systems:${NC}"
    MODELS_TO_PULL=(
        "qwen2.5-coder:1.5b"
        "mistral:latest"
    )
fi

# Pull each model
echo -e "\n${YELLOW}Pulling models (this may take 10-30 minutes):${NC}"
for model in "${MODELS_TO_PULL[@]}"; do
    # Check if model already exists
    if ollama list | grep -q "$model"; then
        echo -e "${GREEN}✓ $model already present${NC}"
    else
        echo -e "${YELLOW}→ Pulling $model...${NC}"
        if ollama pull "$model"; then
            echo -e "${GREEN}✓ $model downloaded${NC}"
        else
            echo -e "${RED}✗ Failed to pull $model${NC}"
        fi
    fi
done

# Step 4: Verify models
echo -e "\n${YELLOW}Step 4: Verifying models...${NC}"
ollama list

# Step 5: Test models
echo -e "\n${YELLOW}Step 5: Testing models...${NC}"

MODELS_INSTALLED=$(ollama list | awk 'NR>1 {print $1}')

for model in $MODELS_INSTALLED; do
    echo -e "${YELLOW}  Testing $model...${NC}"
    if echo "respond with just the word 'ok'" | timeout 30 ollama run "$model" > /dev/null 2>&1; then
        echo -e "${GREEN}  ✓ $model responsive${NC}"
    else
        echo -e "${YELLOW}  ⚠ $model may need warmup${NC}"
    fi
done

# Step 6: Configuration summary
echo -e "\n${GREEN}===============================================${NC}"
echo -e "${GREEN}Installation Complete!${NC}"
echo -e "${GREEN}===============================================${NC}\n"

echo -e "${YELLOW}Configuration Summary:${NC}"
echo -e "  OS: $OS_TYPE"
echo -e "  Hardware: $HARDWARE"
echo -e "  Ollama Version: $(ollama --version 2>/dev/null || echo 'unknown')"
echo -e "  Models: $(ollama list | wc -l) installed"

echo -e "\n${YELLOW}Next Steps:${NC}"
echo -e "  1. Read: COMPREHENSIVE_COST_ANALYSIS_FRAMEWORK_V2.md"
echo -e "  2. Use: decision-trees/01-what-is-my-task.md for your first task"
echo -e "  3. Log: Use templates/task-log-template.md to track tasks"
echo -e "  4. Monthly: Use templates/monthly-report-comprehensive.md for analysis"

echo -e "\n${YELLOW}Start using models:${NC}"
echo -e "  Interactive: ollama run qwen2.5-coder:7b"
echo -e "  API: curl http://localhost:11434/api/generate -d '{\"model\": \"qwen2.5-coder:7b\", \"prompt\": \"hello\"}'"

echo -e "\n${GREEN}Happy coding!${NC}\n"
