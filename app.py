from fastapi import FastAPI
from View import usuario_view , persona_view
from Database import coneccion

app = FastAPI()

'''
Importamso las vistas que estan en el Usuario_view,
hacemos lo mismo con todas las vistas que quieran
importarse.

Nota: Toda logica ruta que se asocie al Usuario se
pociciona dentro de la vista.

Si es necesario importar mas vista, se llamaran de 
la msima forma pero haciendo referencia al objeto
correspondiente. 
'''
app.include_router(usuario_view.router)
app.include_router(persona_view.router)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.on_event("startup")
async def startup_event():
    coneccion.connect()
    coneccion.create_table_usuario()
    coneccion.create_person_table()