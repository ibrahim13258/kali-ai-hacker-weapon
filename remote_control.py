import paramiko
import socket
import threading
from flask import Flask, request, jsonify

app = Flask(__name__)

class SecureRemoteControl:
    def __init__(self):
        self.ssh_client = paramiko.SSHClient()
        self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    def connect_ssh(self, host, username, password=None, key_path=None):
        try:
            if key_path:
                self.ssh_client.connect(host, username=username, key_filename=key_path)
            else:
                self.ssh_client.connect(host, username=username, password=password)
            return True
        except Exception as e:
            return str(e)
    
    def execute_remote(self, command):
        stdin, stdout, stderr = self.ssh_client.exec_command(command)
        return stdout.read().decode(), stderr.read().decode()
    
    def transfer_file(self, local_path, remote_path):
        sftp = self.ssh_client.open_sftp()
        sftp.put(local_path, remote_path)
        sftp.close()
        return f"File transferred to {remote_path}"

@app.route('/api/command', methods=['POST'])
def execute_command():
    data = request.json
    command = data.get('command')
    result = remote_control.execute_remote(command)
    return jsonify({"output": result})

if __name__ == "__main__":
    remote_control = SecureRemoteControl()
    app.run(host='0.0.0.0', port=5000, ssl_context='adhoc')
