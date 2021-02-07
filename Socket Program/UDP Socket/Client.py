###import module socket
import socket

###buat pesan yang akan dikirimkan ke server dengan encode UTF-8
UDP_Massage = bytes('halo dunia', 'UTF-8')

###buat UDP Stream yang digunakan untuk menangkap komunikasi dari server
UDP_Client_Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDP_Client_Socket.sendto(UDP_Massage, ('127.0.0.1', 6500))

