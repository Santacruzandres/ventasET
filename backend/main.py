import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from fastapi_sqlalchemy import DBSessionMiddleware, db

import schema
from models import Producto
from models import Producto as ModelProducto

load_dotenv(".env")

app = FastAPI()

app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/productos")
def get_productos():
    productos = db.session.query(Producto).all()
    return productos

@app.post("/crear-producto/", response_model=schema.Producto)
def crear_producto(producto: schema.Producto):
    db_producto = ModelProducto(referencia=producto.referencia, descripcion=producto.descripcion, condicion=producto.condicion, precio=producto.precio)
    db.session.add(db_producto)
    db.session.commit()
    return db_producto


if __name__ == "__main__":
  uvicorn.run(app, host="0.0.0.0", port=8000)