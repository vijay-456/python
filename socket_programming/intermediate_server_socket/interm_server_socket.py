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

   file = "src.txt"
   fp = open(file, "r")
   print("Opening the file ....")
   data = fp.readlines()
   print("Transfering the data ...")
   count = len(data)

   for line in data:
      record = line.split()[0]
      #print(record)
      resp = connection.recv(1024).decode("utf-8")

      curr_time = str(datetime.datetime.now() + datetime.timedelta(hours=5.5))
      if count != 1 :
        dat = record+','+str(curr_time)+','+'YES'
      else :
        dat = record+','+str(curr_time)+','+'NO'
    
      if resp == 'send':
         connection.send(dat.encode('utf-8'))
      else :
         pass

   fp.close()
   print("Closing the file ......")
   if fp.closed:
      print("File closed successfully.")

   connection.close()                # Close the connection
   print('Connection closed for ', addr, ' at ', curr_time)
