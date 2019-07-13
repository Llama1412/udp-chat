import socket
import threading

connected_ips = []

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(("0.0.0.0",9999))

while True:
	data, addr = server.recvfrom(4096)
	if addr not in connected_ips:
		connected_ips.append(addr)
		print("[*] New connection from " + str(addr[0])+":"+str(addr[1]))
