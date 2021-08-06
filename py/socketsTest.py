import socket
import time
import pickle

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 3232))
s.listen(5)

while True:
    print('Waiting for connection...')
    clientsocket, address = s.accept()
    print(f"connection from {address} has been setup")

    d = {1: "waka", 2:"nda", 3: "nator"}
    msg = pickle.dumps(d)
    print(msg)  
    msg = bytes(f'{len(msg):<{HEADERSIZE}}', "utf-8")+msg


    clientsocket.send(msg)
    clientsocket.close()
    
    # while True:
    #     time.sleep(3)
    #     msg = f"Connection active"
    #     msg = f"{len(msg):<{HEADERSIZE}}"+msg
    #     clientsocket.send(bytes(msg, "utf-8"))
    #     # if input() == 'close':
    #     #     clientsocket.close()
    #     #     break