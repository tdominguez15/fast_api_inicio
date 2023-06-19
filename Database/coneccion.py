import sqlite3

def connect():
    conn = sqlite3.connect('App.db')
    return conn

def create_table_usuario():
    conn = connect()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY,
                  nombreUsuario TEXT NOT NULL,
                  email TEXT NOT NULL,
                  fechaAlta DATE,
                  telefono TEXT,
                  contraseña TEXT)''')
    conn.commit()
    conn.close()

def create_person_table():
    conn = connect()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS person
                 (id INTEGER PRIMARY KEY,
                  CUIT TEXT NOT NULL,
                  razonSocial TEXT NOT NULL,
                  user_id INTEGER NOT NULL,
                  fechaFundacion DATE NOT NULL,
                  FOREIGN KEY (user_id) REFERENCES users(id))''')
    conn.commit()
    conn.close()