print("UDP Chat App with Multi-Threading")
# importing modules for the chat app
import socket
import time
import threading
import sys

# Function for receiving
def receiver():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ipSender, portSender)) #binding the IP address and port number
    while True:
        message = sock.recvfrom(1024)
        print("\n"+message[0].decode())
        if "CLOSEthis" in message[0].decode():
            sys.exit()

#Function for sending
def sender():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = "hello"
    while True:
        if "CLOSEthis" in text:
            exit()
        else:
            text = input(f'{name}:')
            text = name+":"+text
            sock.sendto(text.encode(), (ipReceiver, portReceiver))


if __name__ == "__main__":
    rendezvous = ('192.168.56.1', 55555)

    # connect to rendezvous
    print('connecting to rendezvous server')

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('0.0.0.0', 50001))
sock.sendto(b'0', rendezvous)

while True:
    data = sock.recv(1024).decode()

    if data.strip() == 'ready':
        print('checked in with server, waiting')
        break

    data = sock.recv(1024).decode()
    ip, sport, dport = data.split(' ')
    sport = int(sport)
    dport = int(dport)

    print('\ngot peer')
    print('  ip:          {}'.format(ip))
    print('  source port: {}'.format(sport))
    print('  dest port:   {}\n'.format(dport))

    # punch hole
    # equiv: echo 'punch hole' | nc -u -p 50001 x.x.x.x 50002
    print('punching hole')

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', sport))
    sock.sendto(b'0', (ip, dport))

    print('ready to exchange messages\n')


    name = input("Enter Username: ")
    ipSender = socket.gethostbyname(socket.gethostname())
    print(ipSender)
    ipPair = {name:ipSender}
    portSender = int(input("\nEnter the port of your system: "))

    receiving = threading.Thread(target=receiver)
    receiving.start()

    ipReceiver = input("\nEnter the IP of chat partner: ")
    portReceiver = int(input("\nEnter the port of chat partner: "))

    print("Waiting for client....")
    time.sleep(1)
    print("Connection established....")

    # Using Multi-threading
    sending = threading.Thread(target=sender)
    sending.start()
