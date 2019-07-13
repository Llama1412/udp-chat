import socket
import threading
import time

connected_ips = {}

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(("0.0.0.0",9999))

def clean_ips():
	while True:
		time.sleep(10)
		global connected_ips
		new_connected_ips = {}
		print("[*] There are "+str(len(connected_ips))+" clients connected.")
		for key in connected_ips:
			last_time = connected_ips[key][0]
			delta = time.time() - last_time
			if delta > 10:
				print("Removing "+str(key))
			else:
				new_connected_ips[key] = [last_time, connected_ips[key][0]]
		connected_ips = new_connected_ips

cleaner = threading.Thread(target=clean_ips)
cleaner.daemon = True
cleaner.start()

def handle_message(message, sender):
	for key in connected_ips:
		if sender[0] != key:
			server.sendto(message.encode(),(key, 9998))


while True:
	data, addr = server.recvfrom(4096)
	if addr[0] not in connected_ips.keys() and data.decode().startswith("I am "):
		name = " ".join(data.decode().split(" ")[2:])
		print("[*] New connection from " + str(addr[0])+":"+str(addr[1]) + " called "+name)
		connected_ips[str(addr[0])] = [time.time(), name]
	else:
		connected_ips[str(addr[0])] = [time.time(), connected_ips[str(addr[0])][1]]
		message = data.decode()
		print(message)
		threading.Thread(target=handle_message, args=(message,addr)).start()
