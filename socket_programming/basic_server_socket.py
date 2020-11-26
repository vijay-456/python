import socket               # Import socket module
import datetime

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 8081             # Reserve a port for your service.
sock.bind((host, port))        # Bind to the port
print(host,port)
sock.listen(5)                 # Now wait for client connection.
while True:
   connection, addr = sock.accept()     # Establish connection with client.
   curr_time = str(datetime.datetime.now()+datetime.timedelta(hours=5.5))
   print('Got connection from', addr,' at ',curr_time)
   data = 'Thank you for connecting, successs ra vijay at '+curr_time
   data = bytes(data,'ascii')
   connection.sendall(data)
   connection.close()                # Close the connection