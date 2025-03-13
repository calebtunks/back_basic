import socket
#import time
#import nmap
import argparse
#victom ip = 127.0.0.1
#PORT = 4000

parser = argparse.ArgumentParser(
    description="Simple backend"
)

parser.add_argument("--ip", type=str, required=True)
parser.add_argument("--port", type=int, default=4000, required=False)

def connect(): #return socket
    args = parser.parse_args()
    
    s = socket.socket()
    s.bind((args.ip, args.port))
    s.listen(1)
    
    conn, addr = s.accept()
    
    while True:
        line = input()
        if line == 'exit':
            break
        else:
            conn.send(line.encode())
            print(f"Sent: {line}")
            data = conn.recv(1024).decode()
            print(f"Received: {data}")

    
def main():
    while True:
        s = connect()
        print("Connected to ATT server")
        s.close()
        print("Disconnected from ATT server")
        
        
        
if __name__ == "__main__":
    main()