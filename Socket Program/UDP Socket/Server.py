###import module
import socket

###membentuk komunikasi menggunakan UDP
Server_Socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

###membuat koneksi dengan UDP
Server_Socket.bind(('127.0.0.1', 6500))

###menerima paket yang dikirim client ke server
UDP_Data, UDP_Recive = Server_Socket.recvfrom(1024)

###decode paket yang teleh dikirim client dari byte ke string
print('data =', bytes.decode(UDP_Data))
