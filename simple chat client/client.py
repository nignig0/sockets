import socket
import threading

#client code
#Trying to build a chat room and this is the code
#for every chat client

def listen_for_messages(socket):
    #we keep listening for anything from the server

    while True:
        data= socket.recv(1024)
        #we pause and listen here
        #If there's something, we display
        if data:
            print()
            print(data.decode('utf-8'))

def start_client():
    try:
        username = input("Enter your username: ")
        
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Trying to connect')
        s.connect(('127.0.0.1', 12345))
        print('Connected to the server!')
        print('Enter your message! To disconnect, press q')
        thread = threading.Thread(target = listen_for_messages, args = (s,))
        thread.start()
        message = ''
        while message!= 'q':
            message = input()
            s.sendall(f"{username}: {message}".encode('utf-8'))
    
        s.close()
        exit()
    except Exception as e:
        print(e)
        
start_client()