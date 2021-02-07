###import module yang diperlukan
import os
import socket

'''
karena yang operating system yang digunakan adalah ubuntu maka perintah untuk membersihkan
layar adalah clear
'''
os.system('clear')

print('UDP Server\n\n')

###membentuk komunikasi UDP
UDP_Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

###membuat komunikasi UDP dengan ip address dan port yang akan digunakan
UDP_Socket.bind(('127.0.0.1', 6500))

###looping
while True:
    ###menerima paket yang dikirimkan oleh client
    UDP_Transmit = UDP_Socket.recv(1024)

    ###menampilkan dan mendecode paket yang berasal dari client (byte -> string)
    print('>>>', bytes.decode(UDP_Transmit))
