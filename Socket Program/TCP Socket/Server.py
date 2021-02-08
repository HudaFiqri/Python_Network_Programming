#import module yang akan digunakan
import socket
import os

'''
karena os yang digunakan pembuat adalah linux/ubuntu maka untuk membersihkan layar terminal
perintahnya adalah [ clear ].
dan untuk os yang menggunakan windows bisa menggunakan [ cls ].
'''

os.system('clear')
print('TCP Server\n\n')

###membuat modul yang diperlukan untuk membuat tcp stream
TCP_Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

###membuat TCP server host
TCP_Socket.bind(('127.0.0.1', 6500))

###server menunggu paket yang akan dikirimkan
TCP_Socket.listen()

while True:

    ###membuat TCP menerima paket yang dikirimkan oleh client
    TCP_Receive, TCP_Address = TCP_Socket.accept()

    ###menampilkan paket yang diterima oleh server
    TCP_Data = TCP_Receive.recv(1024)

    ###men-decode paket yang diterima oleh server yang berasal dari byte menjadi string
    print('>>>', bytes.decode(TCP_Data))
