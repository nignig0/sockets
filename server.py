#server code
import socket

def start_server():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('127.0.0.1', 12345))
        s.listen(2)
        print('Listening for connections')
        
        conn, addr = s.accept()
        print(f'Connection from {addr}')
        
        while True:
            data = s.recv(1024)
            if data:
                s.sendall(data)
        conn.close()
        s.close()
    except Exception as e:
        print(e)
        
start_server()
    