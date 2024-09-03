import socket

#client code
#Trying to build a chat room and this is the code
#for every chat client

def start_client():
    try:
        username = input("Enter your username: ")
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Trying to connect')
        s.connect(('127.0.0.1', 12345))
        print('Connected to the server!')
        print('To disconnect, press q')
        message = ''
        while message!= 'q':
            data = s.recv(1024)
            if data:
                print(data)
            message = input('Enter a message to send to the server')
            s.sendall(f'{username}: {message}').encode('utf-8')
    
        s.close()
    except Exception as e:
        print(e)
        
start_client()