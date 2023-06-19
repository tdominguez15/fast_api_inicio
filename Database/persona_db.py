from Model.persona import Persona
from Model.usuario import User
from Database import coneccion

def create_person(person: Persona):

    conn = coneccion.connect()
    c = conn.cursor()
    c.execute('''INSERT INTO person (CUIT, razonSocial, fechaFundacion ,user_id)
                 VALUES (?, ?, ?, ?)''', (person.CUIT, person.razonSocial, person.fechaFundacion, person.user.id))
    conn.commit()
    conn.close()

    return {"message": "Person created successfully"}


def get_person(person_id: int):
    conn = coneccion.connect()
    c = conn.cursor()
    c.execute('''SELECT p.CUIT, p.razonSocial, p.fechaFundacion, p.fechaFundacion, u.nombreUsuario, u.email 
                 FROM person p
                 JOIN users u ON p.user_id = u.id
                 WHERE p.id = ?''', (person_id,))
    result = c.fetchone()
    conn.close()
    if result is None:
        return {"message": "Person not found"}
    person = Persona(id=person_id, CUIT=result[0], razonSocial=result[1], fechaFundacion=result[2],
                    user=User(nombreUsuario=result[3], email=result[4]))
    return person

def delete_person_from_database(persona_id: int):
    conn = coneccion.connect()
    c = conn.cursor()
    c.execute("DELETE FROM persona WHERE id=?", (persona_id,))
    conn.commit()
    conn.close()