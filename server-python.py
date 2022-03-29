###############################################################################
# server-python.py
# Name: Talbot Taylor
# BU ID: U42035349
# Email: talbotct@bu.edu
###############################################################################

import sys
import socket

RECV_BUFFER_SIZE = 2048
QUEUE_LENGTH = 10

def server(server_port):
    """TODO: Listen on socket and print received message to sys.stdout"""
    #opens sock
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sets up ip stuff
    s.bind(('127.0.0.1', server_port))

    #listen for queue length 10
    s.listen(QUEUE_LENGTH)
    
    #infinite loop to recieve
    while 1:
        #accepts connection and recieves data
        conn,addr=s.accept()
        
        data=conn.recv(RECV_BUFFER_SIZE)

        #while theres data coming through write the data out
        #and flush to flush the buffer
        #set data again to prevent a bunch of extra coming through
        while data:    
            sys.stdout.write(data)
            sys.stdout.flush()

            data=conn.recv(RECV_BUFFER_SIZE)
    #close sock        
    conn.close()

def main():
    """Parse command-line argument and call server function """
    if len(sys.argv) != 2:
        sys.exit("Usage: python server-python.py [Server Port]")
    server_port = int(sys.argv[1])
    server(server_port)

if __name__ == "__main__":
    main()
