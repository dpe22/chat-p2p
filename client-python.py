###############################################################################
# client-python.py
# Name: Talbot Taylor
# BU ID: U42035349
# Email: talbotct@bu.edu
###############################################################################

#https://www.youtube.com/watch?v=5za6eRdHjpw&ab_channel=anthonywritescode
#https://www.youtube.com/watch?v=VJ_yNiFzyX4&ab_channel=mr.1n5an_e
#https://www.youtube.com/watch?v=Lbfe3-v7yE0&ab_channel=sentdex
#https://www.youtube.com/watch?v=6mCBmRRwt7k&ab_channel=SanjayGupta
#https://www.youtube.com/watch?v=3QiPPX-KeSc&ab_channel=TechWithTim
#I found the above videos quite helpful for general knowledge   ``
#I also found piazza @220 to be very useful as well

import sys
import socket

SEND_BUFFER_SIZE = 2048

def client(server_ip, server_port):
    """TODO: Open socket and send message from sys.stdin"""
    
    #opens sock
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #connects to server
    s.connect((server_ip, server_port))
    
    #looks for message to take in and then send until through all
    for mess in sys.stdin:
        sys.stdout.write(mess)

        s.sendall(mess) 
        #remove hello world

    #close sock
    s.close()

def main():
    """Parse command-line arguments and call client function """
    if len(sys.argv) != 3:
        sys.exit("Usage: python client-python.py [Server IP] [Server Port] < [message]")
    server_ip = sys.argv[1]
    server_port = int(sys.argv[2])
    client(server_ip, server_port)

if __name__ == "__main__":
    main()
