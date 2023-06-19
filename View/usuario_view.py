from Model.usuario import User
from fastapi import APIRouter
from Database import usuario_db

router = APIRouter()

@router.post("/users/")
async def create_user(user: User):
    # lógica para crear el usuario aquí
    
    is_telefono_valido = user.validarTelefono()
    is_fecha_valida = user.validarFechaAlta()
    
    if is_telefono_valido and is_fecha_valida:
        usuario_db.create_user_in_database(user)
        return {"message": "Usuario creado exitosamente"}        
    else:
        return {"message": "El usuario no se ha podido generar exitosamente"}

@router.get("/users/{user_id}")
async def get_user(user_id: int):
    user = usuario_db.get_user_from_database(user_id)
    if user:
        return user.dict()
    else:
        return{"message": "Usuario no Encontrado"}

@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    usuario_db.delete_user_from_database(user_id)
    return {"message": "Usuario eliminado exitosamente"}

@router.put("/users/{user_id}")
async def update_user(user_id: int, user: User):

    is_telefono_valido = user.validarTelefono()
    is_fecha_valida = user.validarFechaAlta()
    
    if is_telefono_valido and is_fecha_valida:
        user.id = user_id
        usuario_db.update_user_in_database(user)
        return {"message": "Usuario actualizado exitosamente"}        
    else:
        return {"message": "El usuario no se ha podido actualizar los datos exitosamente"}
