# Echo client program
import socket
import rsa

flag = True
serv_key = rsa.PublicKey(0,0)
HOST = 'awsomkiller'  # The remote host
PORT = 50000  # The same port as used by the server
msg = input("Enter command (type exit to exit):")
byte = msg.encode('utf-8')
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b'requestkey')
    recv = s.recv(1024)
    serv_key = serv_key.load_pkcs1(recv)
    while flag:
        crypto = rsa.encrypt(byte,serv_key)
        s.sendall(crypto)
        data = s.recv(1024)
        output = data.decode('utf-8')
        print(output)
        msg = input("Enter command (type exit to exit) :")
        if msg == 'exit':
            flag = False
        byte = msg.encode('utf-8')

