import socket               # Import socket module

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # Get local machine name
#host = '172.168.1.6'      #using local ip to connect to remote machine.
port = 8081               # Reserve a port for your service.
print(host,port)
sock.connect((host, port))
print(sock.recv(1024).decode('utf-8'))
sock.close()                     # Close the socket when done