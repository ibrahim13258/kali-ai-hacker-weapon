mkdir ~/ai-assistant && cd ~/ai-assistant
python3 -m venv ai-env
source ai-env/bin/activate

# Install AI dependencies
pip install torch torchvision torchaudio
pip install transformers sentencepiece protobuf
pip install speechrecognition pyttsx3 pyaudio
pip install flask requests paramiko
