import socket
import random
import time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



while True:
    hr_test = random.randint(40,200)
    msg = "2,{:d},C,,\"75\",".format(hr_test)
    server_address = ("127.0.0.1", 8909) 
    client_socket.sendto(msg.encode(), server_address)
    time.sleep(0.8)
