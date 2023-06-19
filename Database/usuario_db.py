from Model.usuario import  User
from Database import coneccion

def create_user_in_database(user: User):
    conn = coneccion.connect()
    c = conn.cursor()
    c.execute("INSERT INTO users (nombreUsuario, email, fechaAlta, telefono, contraseña) VALUES (?, ?, ?, ?, ?)",
              (user.nombreUsuario, user.email, user.fechaAlta, user.telefono, user.contraseña))
    user_id = c.lastrowid
    conn.commit()
    conn.close()
    return {"message": "User created successfully", "user_id": user_id}

def get_user_from_database(user_id: int) -> User:
    conn = coneccion.connect()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE id=?", (user_id,))
    row = c.fetchone()
    if row:
        user = User(id=row[0], nombreUsuario=row[1], email=row[2], fechaAlta=row[3], telefono=row[4], contraseña=row[5])
        conn.close()
        return user
    else:
        conn.close()
        return None

def delete_user_from_database(user_id: int):
    conn = coneccion.connect()
    c = conn.cursor()
    c.execute("DELETE FROM users WHERE id=?", (user_id,))
    conn.commit()
    conn.close()

def update_user_in_database(user: User):
    conn = coneccion.connect()
    c = conn.cursor()
    c.execute("UPDATE users SET nombreUsuario=?, email=?, fechaAlta=?, telefono=?, contraseña=? WHERE id=?", (user.nombreUsuario, user.email, user.fechaAlta, user.telefono, user.contraseña, user.id))
    conn.commit()
    conn.close()
