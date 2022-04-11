
import socket
import os
from my_protocol import MY_PROTOCOL

HOST = '127.0.0.1'
PORT = 4444


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)



mp = MY_PROTOCOL()

conn, addr = s.accept()


def execute_command(command):
    os.system(command + " > output.txt")
    file = open("output.txt", 'r')
    message = file.read()
    
    print("-------------------------------------------------",len(message))
    #print(message)
    mp.send_message(conn = conn, src = '127.0.0.1', dst = '127.0.0.1', message = message)

while(True):
    package = mp.receive_message(conn)

    execute_command(package['message'])
