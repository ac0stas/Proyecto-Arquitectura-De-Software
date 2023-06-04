import socket
import sqlite3
from utils import bus_format

def login(nombre, clave):
    con = sqlite3.connect("db.sqlite3")
    cursor = con.cursor()
    query = f"""SELECT * FROM usuarios WHERE Nombre = '{nombre}' AND Clave = '{clave}' ;"""
    cursor.execute(query)
    rows = cursor.fetchall()
    con.commit()
    con.close()
    if (len(rows) == 0):
        return None
    else:
        return rows[0]


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5000)
sock.connect(server_address)

message = b"00050sinitserv0"
sock.sendall(message)
status = sock.recv(4096)[10:12].decode('UTF-8')

print(status)
if (status == 'OK'):
    print('Servicio login iniciado de forma correcta\n')
    while True:
        received_message = sock.recv(4096).decode('UTF-8')
        print(received_message)
        client_id = received_message[5:10]
        data = eval(received_message[10:])
        ans = login(data['Nombre'], data['Clave'])
        response = bus_format(ans, str(client_id)).encode('UTF-8')
        sock.send(response)
