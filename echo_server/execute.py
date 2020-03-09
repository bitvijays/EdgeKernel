import os
import threading
import socket
import sys
import multiprocessing
import time


def server():
    sock_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('10.0.0.1', 1339)
    sock_c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    router_address = ('10.0.0.1', 1338)
    print '[PYTHON] starting up on %s port %s' % server_address
    sock_s.bind(server_address)
#    sock_s.connect(("10.0.0.42",1337))
#    print "connected to 10.0.0.42:1337"
    print '[PYTHON] starting up on %s port %s' % router_address
    sock_c.bind(router_address)
    sock_c.listen(5)
    count = 0
    data = "TEST"
    #    while count < 1:
    #    if count == 0:
    # Wait for a connection
    connection, client_address = sock_c.accept()
    print '[PYTHON] connection from', client_address
    data = connection.recv(1024)
    print(data)
    sock_s.connect(("10.0.0.42",1337))

    sock_s.send(data)
#    time.sleep(3)
    in_data = sock_s.recv(1024)
#   time.sleep(3)
    print("[PYTHON] Server Sends: " + in_data)
    connection.send(in_data)
    #count += 1
        
    print "[PYTHON] Exiting"
    sock_s.shutdown(socket.SHUT_RDWR)
    sock_s.close()
    sock_c.shutdown(socket.SHUT_RDWR)
    sock_c.close()
    exit()


def unikernel_server():
    os.system("boot build/tcp_service")

def unikernel_client():
    os.system("boot build/tcp_client")
            
def main():
    try:
        s = multiprocessing.Process(target=unikernel_server)
        p = multiprocessing.Process(target=server)
        c = multiprocessing.Process(target=unikernel_client)
        #        s.start()        
        p.start()
        #unikernel_client()
        #c.start()
        p.join()

#        c.start()
    except:
        print "Cannot Open New Thread"


if __name__ == '__main__':
    main()
