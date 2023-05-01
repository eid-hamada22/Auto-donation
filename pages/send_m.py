from socket import *

IP = '192.168.0.107'

def SendProto(conn, d):
    # send dictionary lingth:
    if conn.recv(1) == chr(0).encode('utf-8'):
        conn.send(len(d.keys()).__str__().encode('utf-8'))
        conn.recv(1) # Synchronizer
    # looging through the whole thing:
    for dic in d.keys():
        # Define Requerments:
        key = dic; data = d[dic]
        dtype = type(d[dic]).__name__
        # send Key & Type:
        if conn.recv(1) == chr(1).encode('utf-8'): conn.send(key.encode('utf-8'))
        if conn.recv(1) == chr(2).encode('utf-8'): conn.send(dtype.encode('utf-8'))
        ## Slice & Send:
        v = d[dic]
        # Encoding process:
        if type(v).__name__ == 'bytes': value = v
        elif type(v).__name__ == 'str': value = v.encode('utf-8')
        elif type(v).__name__ == 'int': value = v.__str__().encode('utf-8')
        else: value = str(v).encode('utf-8')
        # Sending the data size:
        conn.recv(1)
        conn.send(len(value).__str__().encode('utf-8'))
        # sending:
        conn.recv(1)
        conn.sendall(value)
        conn.recv(1)

#  Custom Receiving protocol:
def RecvProto(conn, buffersize=1024, dump=True):
    # recv dictionary lingth:
    conn.send(chr(0).encode('utf-8'))
    length = int(conn.recv(1024))
    conn.send(chr(0).encode('utf-8'))
    # Getting the dictionary data:
    d = {}
    for dic in range(length):
        # receive Key & Type:
        conn.send(chr(1).encode('utf-8'))
        key = conn.recv(1024).decode('utf-8')
        conn.send(chr(2).encode('utf-8'))
        dtype = conn.recv(1024).decode('utf-8')
        ## Receive the value fragments and Reassemble them:
        # Receiving data:
        conn.send(b'0')
        SIZE = int(conn.recv(1024))
        conn.send(b'0')
        v = b''
        while (v.__len__() != SIZE):
            v += conn.recv(buffersize)
        conn.send(b'0')
        # Decoding:
        if dtype == 'bytes': value = v
        elif dtype == 'str': value = v.decode('utf-8')
        elif dtype == 'int': value = int(v)
        else: value = v.decode('utf-8')
        d[key] = value
    if dump: return d
    else: conn.__class__.payload = d

conn = socket(AF_INET, SOCK_STREAM)
conn.connect((IP, 8080))
port = int(conn.recv(1024))

server = socket(AF_INET, SOCK_STREAM)
server.connect((IP, port))
server.send(chr(0).encode('utf-8'))

# phone: '05687657899087', msg = 'text'
def SendMSG(num, msg): 
    server.send(chr(1).encode('utf-8'))
    SendProto(server, {
        'num': num,
        'msg':   msg
    })
    return bool(int(server.recv(1)))

# while True:
#     if SendMSG(Num, input("MSG : ")):
#         print('Done')
#     else:
#         print('Error:')