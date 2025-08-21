import os
import subprocess
import json
import speech_recognition as sr
import pyttsx3
import paramiko
from transformers import AutoTokenizer, AutoModelForCausalLM
import threading

class KaliAIAssistant:
    def __init__(self):
        self.model_path = "meta-llama/Meta-Llama-3-8B-Instruct"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_path)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_path)
        self.engine = pyttsx3.init()
        
    def listen(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            return None
    
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
    
    def execute_command(self, command):
        try:
            result = subprocess.run(command, shell=True, 
                                  capture_output=True, text=True, 
                                  timeout=30)
            return result.stdout if result.returncode == 0 else result.stderr
        except Exception as e:
            return str(e)
    
    def process_query(self, query):
        # AI processing logic
        response = self.generate_response(query)
        
        # Check for system commands
        if "run tool" in query.lower():
            tool = query.split("run tool")[-1].strip()
            return self.execute_kali_tool(tool)
        
        return response
    
    def generate_response(self, prompt):
        inputs = self.tokenizer(prompt, return_tensors="pt")
        outputs = self.model.generate(**inputs, max_length=200)
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    def execute_kali_tool(self, tool_name):
        # Map tool names to commands
        tool_commands = {
            "nmap": "nmap -sS -sV",
            "metasploit": "msfconsole -q",
            "wireshark": "wireshark",
            # Add more tools as needed
        }
        
        if tool_name in tool_commands:
            return self.execute_command(tool_commands[tool_name])
        return f"Tool {tool_name} not found in database"
