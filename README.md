# chat-p2p
Peer to Peer Chat Module

[![Python Lint Test](https://github.com/dpe22/chat-p2p/actions/workflows/python-lint-test.yml/badge.svg)](https://github.com/dpe22/chat-p2p/actions/workflows/python-lint-test.yml)

Give me a call to work during class: 3019228272 - Talbot 
## Sources:

- https://medium.com/swlh/rabbitmq-developing-message-based-applications-a56003c55649
- https://www.geeksforgeeks.org/simple-chat-room-using-python/ 
- https://realpython.com/python-sockets/ 


## Progress report:
- "basicSocketProject" branch has threaded program that could take two clients and connect them to eachother
- client-python and server-python codes are basic socket programming files that can communicate basic messaging features with others
- Since the server.py in basicSocketProgramming branch is unable to recognize users outside the system, we have setup client-python.py and server-python.py to be able to communicate with outside systems

## Completed project functionality 
- Chat room

- Pull this repository and run server on a device with inbound and outbound traffic enabled on the selected port:
```bash

python P2P-Threaded_Server.py [Server IP] [Server Port]

```

- On a different terminal, or another device become a client by entering:
```bash

python P2P-Threaded_Client.py [Server IP] [Server Port]

```

    Enter username and begin chatting with other users in the chat room