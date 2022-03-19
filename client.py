#!python3 

import socket 
HEADER = 64
PORT= 5000
DISCONNECT_MESSAGE = "!DISCONNECT"
FORMAT = 'utf-8'
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect (ADDR)

def send(msg):
    message= msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
   

# does not really do anything I used a template for most of this too and it really just does a whole lot of nothing I under
# stand more of what it does after using it in the API for M C but did not have time to add much to it besides tell me if
# there was a connection


# Additions I am making... getting rid of it and learning node cause it's prettier
 