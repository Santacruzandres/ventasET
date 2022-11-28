from pydantic import BaseModel


class Producto(BaseModel):
    referencia: int
    descripcion: str
    condicion: str
    precio: int

    class Config:
        orm_mode = True