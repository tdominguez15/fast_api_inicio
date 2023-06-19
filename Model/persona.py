from pydantic import BaseModel
from Model.usuario import User
from datetime import date

class Persona(BaseModel):
    id: int
    CUIT: str
    razonSocial: str
    fechaFundacion: date
    user: User

    def validarDocumento(self):
        
        return True