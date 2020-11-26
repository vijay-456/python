import socket               # Import socket module

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         # Create a socket object
#host = socket.gethostname() # Get local machine name
host = '172.31.44.1'      #using local ip to connect to remote machine.
port = 8081               # Reserve a port for your service.

sock.connect((host, port))
print("Connected to the server ",host,port)

file = "des.txt"
fp = open(file, "a")
print("Opening the file....")
print("Writing into the file ....")

#Requestin for the first record.
sock.send("send".encode('utf-8'))
record = sock.recv(1024).decode("utf-8")
record = record.split(',')
record.pop()
record = ','.join(record)
fp.write(record)


#Requesting for the remaining records.
while True:
    sock.send("send".encode('utf-8'))
    record = sock.recv(1024).decode("utf-8")
    record = record.split(',')
    if record[-1] == 'YES' :
        record.pop()
        record = ','.join(record)
        fp.write(str('\n') + record)
    else :
        record.pop()
        record = ','.join(record)
        fp.write(str('\n') + record)
        break

print("File successfully written.")
fp.close()
print("Closing the file ......")
if fp.closed:
    print("File closed successfully.")
sock.close()                     # Close the socket when done
