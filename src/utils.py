import os
import sqlite3

def bus_format(data, service_name=''):
    transformed_data = str(data)
    transformed_data_len = len(transformed_data)
    digits_left = 5 - len(str(transformed_data_len))
    str_data_length = ''

    for i in range(digits_left):
        str_data_length += '0'

    str_data_length += str(transformed_data_len) + \
        service_name+transformed_data

    return str_data_length

def create_tables():
    conn = sqlite3.connect('db.sqlite3')
    c = conn.cursor()

    c.execute(
        '''CREATE TABLE IF NOT EXISTS users
            (
                rut text PRIMARY KEY,
                email text,
                name text,
                password text,
                type integer DEFAULT 0
            )
            '''

    )
    c.execute(
        '''CREATE TABLE IF NOT EXISTS productos
            (
                id integer PRIMARY KEY AUTOINCREMENT,
                nombre text,
                precio integer,
                stock integer,
                SKU integer,
                categoria text
            )
        '''
    )
    
    conn.commit()
    conn.close()


if __name__ == '__main__':
    crear_tablas()