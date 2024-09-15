#server code
import socket
import threading

client_sockets = [] #list of sockets created for working with the clients
#the sockets here are used for recieving data from the client
#and for pushing data to the client


def handle_client(client_socket):
    try:
        while True:
            #we keep on listening to client data
            print("Listening for client data")
            data = client_socket.recv(1024)
            print("Recieved data")
            if data:
                #if we get data, broadcast to all clients apart from the sender client
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
            #It's like calling a call centre
            #after a call has come in, the customer is then directed to a separate line
            #the separate line is the client socket
            #but the main line keeps listening 
            print(f"connection coming from {addr}")
            client_sockets.append(client_socket)
            thread = threading.Thread(target = handle_client, args = (client_socket,))
            #the thread handles the clients. The separate line. While the main line keeps listening
            thread.start()

        
    except Exception as e:
        print(e)
        
start_server()
    