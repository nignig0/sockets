#server code
import socket
import threading

def listen_for_connection(socket):
    conn, addr = socket.accept()
    print(f'Connection incoming from {addr}')
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect()

def handle_client(client_socket):
    while True:
        data = 

def start_server():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(('127.0.0.1', 12345))
        s.listen(2)
        print('Listening for connections')
        
        thread_one = threading.Thread(target=listen_for_connection, args = (s,), daemon=True)
        #we create a daemon thread that listens for connections in the background

        
        while True:
            data = s.recv(1024)
            if data:
                s.sendall(data)
        conn.close()
        s.close()
    except Exception as e:
        print(e)
        
start_server()
    