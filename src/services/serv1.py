import sqlite3
import sys
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 5000)
sock.connect(server_address)


def create_product(name, price, sku, stock):
    conn = sqlite3.connect('inventario.db')
    c = conn.cursor()
    c.execute("INSERT INTO Product VALUES (?, ?, ?, ?)", (sku, name, price, stock))
    conn.commit()
    conn.close()

try:
    # Send data
    message = b"00050sinitservi1"
    print ('sending {!r}'.format (message))
    sock.sendall(message)
    while True:
        # Look for the response
        print ("Waiting for transaction")
        amount_received = 0
        amount_expected = int(sock.recv (5))
        while amount_received < amount_expected:
            data = data.decode().split()
            print ('received {!r}'.format (data))
            
finally:
    print ('closing socket')
    sock.close ()