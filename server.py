#!python3

import socket
import threading #separate code out 

HEADER = 64
PORT= 5000
SERVER = socket.gethostbyname(socket.gethostname()) #gets us the server 
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #binds socket 
server.bind(ADDR)

def handle_client(conn, addr): #handles communication between client and server 
    print(f"[New Connection] {addr} connected.")

    connected = True 
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) #message into string 
        if msg_length: 
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected= False
            
            print(f"[{addr}] {msg}")
    
    conn.close()


def start(): #individual connection 
    server.listen()
    print(f"[Listening] Server is listening on {SERVER}")
    while True:
        conn, addr, = server.accept() #store address and where it came from 
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[Active Connections] {threading.activeCount() -1}")

print("[STARTING] server starting...")

start()

#if it does not run there is a firewall somewhere 



# does not really do anything I used a template for most of this too and it really just does a whole lot of nothing I under
# stand more of what it does after using it in the API for M C but did not have time to add much to it besides tell me if
# there was a connection. This was more so me learning how to set it up on my own, hence the random comments above



#print("Content-type: text/html")
#print()
#print("<title>Test CGI</title>")
#print("<p>Hello World!</p>")

#generates a string and delivers it to the server 



