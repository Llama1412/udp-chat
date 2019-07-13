import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

target_ip = "127.0.0.1"
target_port = 9999

receiver  = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
receiver.bind(("0.0.0.0",9998))

def handle_incoming(message):
    print(message.decode())

def await_messages():
    while True:
        message, addr = receiver.recvfrom(4096)
        threading.Thread(target=handle_incoming, args=(message,)).start()

# Sign into the server.
name = input("What is your name?\t")
msg = "I am " +str(name)
client.sendto(msg.encode(),(target_ip,target_port))

waiter = threading.Thread(target=await_messages)
waiter.daemon = True
waiter.start()
while True:
    msg = input()
    formatted = name + ":\t" + msg
    client.sendto(formatted.encode(),(target_ip,target_port))
