from fastapi import APIRouter
from Model.persona import Persona
from Database import persona_db , usuario_db

router = APIRouter()

@router.post("/person")
async def create_person(person: Persona):

    return_user = usuario_db.create_user_in_database(person.user)
    is_documento_valido = person.validarDocumento()

    if (return_user.get('message') == 'User created successfully' and is_documento_valido):
        person.user.id = return_user["user_id"]
        persona_db.create_person(person)
        return {"message": "Person created successfully"}
    else:
        return {"message": "Error en la creacion del Usuario"}

@router.get("/person/{person_id}")
async def get_person(person_id: int):
    person = persona_db.get_person(person_id)
    return person

@router.delete("/person/{person_id}")
async def delete_person(user_id: int):
    persona_db.delete_person_from_database(user_id)
    return {"message": "Usuario eliminado exitosamente"}