from fastapi import FastAPI
from typing import Union
from utils import fibonacci


app = FastAPI()


@app.get("/get-value-finobacci-by-index/{index}/")
def get_value_finobacci_by_index(index:int):
    return {"value": fibonacci(index)}