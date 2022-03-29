/*****************************************************************************
 * server-c.c
 * Name: Talbot Taylor
 * BU ID: U42035349
 * Email: talbotct@bu.edu
 *****************************************************************************/

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <netdb.h>
#include <netinet/in.h>
#include <errno.h>

#define QUEUE_LENGTH 10
#define RECV_BUFFER_SIZE 2048

/* TODO: server()
 * Open socket and wait for client to connect
 * Print received message to stdout
 * Return 0 on success, non-zero on failure
*/
int server(char *server_port) {
  // create socket file descriptor
  int server_fd;
  if ((server_fd = socket(AF_INET, SOCK_STREAM, 0)) == 0)
  {
    perror("socket failed");
    exit(EXIT_FAILURE);
  }

  // create socket address
  // forcefully attach socket to the port
  struct sockaddr_in address;
  int opt = 1;
  if (setsockopt(server_fd, SOL_SOCKET, SO_REUSEADDR | SO_REUSEPORT, &opt, sizeof(opt)))
  {
    perror("setsockopt failed");
    exit(EXIT_FAILURE);
  }
  address.sin_family = AF_INET;
  address.sin_addr.s_addr = INADDR_ANY;
  address.sin_port = htons(atoi(server_port));

  // bind socket to address
  if (bind(server_fd, (struct sockaddr *)&address, sizeof(address))<0)
  {
    perror("bind failed");
    exit(EXIT_FAILURE);
  }

  // listen to incoming connections
  if (listen(server_fd, 10) < 0) //changed from 1 to 10 for overlaping clients
  {
    perror("listen failed");
    exit(EXIT_FAILURE);
  }

  // receive message
  char buffer[RECV_BUFFER_SIZE];
  int recvB;
  int sock;
  int addrlen=sizeof(address);
  
  //recv(sock, buffer, RECV_BUFFER_SIZE, 0); moved to while loop

  //similar set up to python nested while loops
  while(1){
    //moved inside to check each time
    if ((sock=accept(server_fd,(struct sockaddr*)&address,(socklen_t*)&addrlen))<0){
      perror("accept failed");
      
      exit(EXIT_FAILURE);
    }

    //loop to write the messages and flush the buffer
    //basically just like original given code but with loop structure
    while(recvB=recv(sock,buffer,RECV_BUFFER_SIZE,0)){
      fwrite(buffer,recvB,1,stdout);

      fflush(stdout);

    }

  }

  //fwrite(buffer, recv_bytes, 1, stdout); to go in while loop
  //fflush(stdout); to go in while loop

  // close socket
  close(sock);

  return 0;
}

/*
 * main():
 * Parse command-line arguments and call server function
*/
int main(int argc, char **argv) {
  char *server_port;

  if (argc != 2) {
    fprintf(stderr, "Usage: ./server-c [server port]\n");
    exit(EXIT_FAILURE);
  }

  server_port = argv[1];
  return server(server_port);
}