import socket
import threading
import base64
import hashlib

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

target_ip = "192.168.1.255"
target_port = 69

client.bind(("0.0.0.0", 69))

def handle_incoming(message, namDome, addr):
    ticker = 0
    msg = message.decode()
    if name + '>' in msg:
        pass
    elif "> FILE " in msg:
        splitup = msg.split(">")[1]
        trimmed = splitup[6:]
        decoded = base64.b64decode(trimmed)
        with open("files/"+ticker, "wb") as file:
            file.write(decoded)
        print("Received a file from " + str(addr[0]) + ". Naming " + str(ticker))
        ticker += 1

    else:
        print(msg + " [" + str(addr[0]) + "]")

def await_messages():
    while True:
        message, addr = client.recvfrom(100000000)
        threading.Thread(target=handle_incoming, args=(message,name,addr,)).start()

name = input("What is your name?\t")
msg = str(name) + " has joined the chat..."
client.sendto(msg.encode(),(target_ip,target_port))

waiter = threading.Thread(target=await_messages)
waiter.daemon = True
waiter.start()

while True:
    msg = input()
    if "SENDFILE" in msg:
        fileName = input("ENTER FILENAME: ")

        file = open(fileName, "rb")
        data = file.read()
        file.close()

        encoded = base64.b64encode(data).decode()
        toSend = name + "> FILE " + encoded
        client.sendto(toSend.encode(), (target_ip,target_port))

    else:
        formatted = name + "> " + msg
        client.sendto(formatted.encode(), (target_ip,target_port))
