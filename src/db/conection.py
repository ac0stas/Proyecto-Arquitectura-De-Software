import sqlite3
import argparse

def configurar_db():
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Productos (
            SKU INTEGER PRIMARY KEY,
            Nombre TEXT NOT NULL,
            Precio REAL NOT NULL,
            Stock INTEGER NOT NULL
        );
    ''')
    conexion.commit()
    conexion.close()

configurar_db()
