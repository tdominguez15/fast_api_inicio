from typing import List
from pydantic import BaseModel
from datetime import date
import re
import datetime

class User(BaseModel):
    id: int = 0
    nombreUsuario: str
    email: str
    fechaAlta: date = date.today()
    contraseña: str = ''
    telefono: str = ''

    def validarTelefono(self):
            '''
            Valida que el campo telefono solo contenga caracteres numericos y no tenga mas de 12 caracteres.
            '''
            # Expresión regular para verificar que el teléfono contenga solo caracteres numéricos
            patron_numerico = '^[0-9]+$'
            
            # Verificar que el teléfono contenga solo caracteres numéricos
            if not re.match(patron_numerico, self.telefono):
                return False
            
            # Verificar que el teléfono tenga como máximo 12 caracteres
            if len(self.telefono) > 12:
                return False
            
            # Si se llega hasta aquí, el teléfono es válido
            return True

    def validarFechaAlta(self):
            '''
            Validar que la Fecha de Alta del Usuario sea igual a la fecha actual
            o menor a la misma en 1 dia.
            '''
            fecha_actual = datetime.datetime.now().date()
            diferencia = self.fechaAlta - fecha_actual
            
            return diferencia.days <= 1
