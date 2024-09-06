#server code
import socket
import threading

client_sockets = []

def handle_client(client_socket):
    try:
        while True:
            print("Listening for client data")
            data = client_socket.recv(1024)
            print("Recieved data")
            if data:
                print('recieved data here')
                for client in client_sockets:
                    if client == client_socket:
                        continue
                    client.sendall(data)
    except Exception as e:
        print("There was an error: ", e)
        client_socket.close()
        client_sockets.remove(client_socket)


def start_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('localhost', 12345))
        server.listen(5)

        while True:
            
            client_socket, addr = server.accept()
            print(f"connection coming from {addr}")
            client_sockets.append(client_socket)
            thread = threading.Thread(target = handle_client, args = (client_socket,))
            thread.start()

        
    except Exception as e:
        print(e)
        
start_server()
    