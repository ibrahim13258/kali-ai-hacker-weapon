#!/bin/bash
cd ~/ai-assistant
source ai-env/bin/activate
python assistant.py &
python remote_control.py &
python monitoring.py &
echo "AI Assistant started successfully"
