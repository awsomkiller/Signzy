#!/usr/bin/python           # This is server.py file

import socket  # Import socket module
import _thread
import os
import rsa

(serv_pub, serv_priv) = rsa.newkeys(1024)               # creating public and private key


def on_new_client(clientsocket, addr):
    flag = True
    while True:
        if flag:
            msg = clientsocket.recv(1024)
            if msg.decode('utf-8') == "requestkey":
                sendkey = serv_pub.save_pkcs1(format='PEM')  # converting pub key to PEM format
                clientsocket.send(sendkey)                   # sending the key to client
                flag = False
        recv = clientsocket.recv(1024)
        msg = rsa.decrypt(recv,serv_priv)
        cmd = msg.decode('utf-8')
        stream = os.popen(cmd)
        output = stream.read()
        # if output == Null:
        #     output = "done"
        outb = output.encode('utf-8')
        clientsocket.send(outb)
    clientsocket.close()


s = socket.socket()  # Create a socket object
host = socket.gethostname()  # Get local machine name
port = 50000  # Reserve a port for your service.

print('Server started!')
print('Waiting for clients...')
print('server running on :', host, 'port :', port)
s.bind((host, port))  # Bind to the port
s.listen(5)  # Now wait for client connection.

while True:
    c, addr = s.accept()  # Establish connection with client.
    print('Got connection from', addr)
    _thread.start_new_thread(on_new_client, (c, addr))
    # Note it's (addr,) not (addr) because second parameter is a tuple
    # Edit: (c,addr)
    # that's how you pass arguments to functions when creating new threads using thread module.
s.close()
