import socket #import for library / to set up a server #

def udp_echo_server(): #dont' forget the import and function call #
    s = socket.socket(type=socket.SOCK_DGRAM) #remember that DGRAM is UDP # socket is the name of the module and the .socket is the name of the object we're creating # (type=) defaults to IPv4 TCP #
    s.bind(('',12345)) #could add IP addy within the quotes # designate the interface we want to connect to # argument is a tuple, whens the double (()) #
    while True:
        data,address = s.recvfrom(4096) #size per datagram (packet?)
        print(data,'received from {}'.format(address))
        s.sendto(data,address) #sending datagrams back to... #

def udp_echo_client(): #dont' forget the import and function call #
    s = socket.socket(type=socket.SOCK_DGRAM)
    s.sendto(b'u haz ben ooned by timboslice' , ('192.168.242.99',12345))
    data,address = s.recvfrom(4096)
    print(data, 'echoed from {}'.format(address))

def tcp_echo_server(): #dont' forget the import and function call #
    s = socket.socket() #don't need to specify TCP, since it's the default #
    s.bind(('',12345))
    s.listen() #!!! one of the main differences between UDP and TCP for socket creation #

    while True:
        conn, address = s.accept()
        print('connection accepted from {}'.format(address))

        data = conn.recv(4096) #echo server needs to receive first and then send back #
        print(data, 'received from {}'.format(address))

        conn.sendall(data) #sendall() will send until done # Doesn't necessarily mean this'll work, since we're just asking to send. Can't force it, obviously #
        conn.close()

def tcp_echo_client(): #dont' forget the import and function call #
    s = socket.socket() #TCP is the default argument #
    s.connect(('192.168.242.99',12345)) #remember, the .connect() argument contains a tuple with the IP and port #
    s.sendall(b'There are some who call me.... Jim.')
    echodata = s.recv(4096) #not gauranteed to work #
    print(echodata, 'echoed from server')


def qotd_client(): #quote of the day server # #dont' forget the import and function call #
    s = socket.socket() #use default #
    s.connect(('djxmmx.net',17))
    received = bytearray()
    buf = s.recv(64) #if that came back with nothing, then it'd close #
    while buf:
        received.extend(buf)
        buf = s.recv(64)

    print(received)


# def qotd_client_try():  # quote of the day server #
#     import time
#     socket.setdefaulttimeout(3)
#     s = socket.socket()
#
#     port = 15
#     while True:
#         try:
#             s.connect(('djxmmx.net', port))
#         except:
#             print('attempt on port {} timed out'.format(port))
#             port += 1
#             time.sleep(1)
#             continue
#         break
#
#     received = bytearray()
#     buf = s.recv(64)  # if that came back with nothing, then it'd close #
#     while buf:
#         received.extend(buf)
#         buf = s.recv(64)
#
#     print(received)


if __name__ == '__main__':
    udp_echo_server()
    udp_echo_client()
    tcp_echo_server()
    tcp_echo_client()
    qotd_client()
    qotd_client_try()


'''in order to use this:
- go to CLI
- navigate to python interpreter with 'python3'
- import sockit #which is the name of the py file#
- then use sockit.udp_echo_client()''' #this is the name of the function I want to use, either the client or server #
#For TCP, a server must be open. So, if you'r using loopback, you must have your own server up. #
