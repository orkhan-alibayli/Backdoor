from importlib.resources import Package
import socket
from my_protocol import MY_PROTOCOL

HOST = '127.0.0.1'
PORT = 4444

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

mp = MY_PROTOCOL()

while(True):    
    command = input('enter command')
    mp.send_message(conn = s, src = '127.0.0.1', dst = '127.0.0.1', message = command)
    package = mp.receive_message(s)
    print('Output is:')
    print(package)
    print(package['message'])