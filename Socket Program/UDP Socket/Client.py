###import module socket
import socket

###looping perintah
while True:
    ###input masukkan
    UDP_Massage = input('masukkan kata = ')

    ###conver dari string menjadi byte
    UDP_Convert = bytes(UDP_Massage, 'UTF-8')

    ###memulai sesi stram UDP
    UDP_Stream = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    ###membentu komunikasi dengan server
    UDP_Stream.sendto(UDP_Convert, ('127.0.0.1', 6500))
