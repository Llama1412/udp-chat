import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

target_ip = "192.168.1.255"
target_port = 69

client.bind(("0.0.0.0", 69))

def handle_incoming(message, name):
    msg = message.decode()
    if(name + '>' in msg):
        pass
    else:
        print(msg)

def await_messages():
    while True:
        message, addr = client.recvfrom(4096)
        threading.Thread(target=handle_incoming, args=(message,name,)).start()

name = input("What is your name?\t")
msg = str(name) + " has joined the chat!"
client.sendto(msg.encode(),(target_ip,target_port))

waiter = threading.Thread(target=await_messages)
waiter.daemon = True
waiter.start()

while True:
    msg = input()
    formatted = name + "> " + msg
    client.sendto(formatted.encode(),(target_ip,target_port))
