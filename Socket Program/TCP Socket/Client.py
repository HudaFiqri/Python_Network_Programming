###import modul yang akan digunakan
import socket
import os

'''
karena os yang digunakan pembuat adalah linux/ubuntu maka untuk membersihkan layar terminal
perintahnya adalah [ clear ].
dan untuk os yang menggunakan windows bisa menggunakan [ cls ].
'''

###clear terminal screen
os.system('clear')
print('TCP Client\n\n')

###looping
while True:

    ###input masukan
    TCP_Input = input('masukkan kata = ')

    ###konvert string menjadi byte
    TCP_Convert = bytes(TCP_Input, 'UTF-8')

    ###membuat modul untuk TCP stream
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    ###membuat koneksi ke server
    s.connect(('127.0.0.1', 6500))

    ###mengirimkan data ke server
    s.sendall(TCP_Convert)
