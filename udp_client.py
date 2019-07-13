import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

target_ip = "127.0.0.1"
target_port = 9999


msg = "hello world"
client.sendto(msg.encode(),(target_ip,target_port))
