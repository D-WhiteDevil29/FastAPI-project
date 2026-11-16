from fastapi import FastAPI
from models import Product

app = FastAPI()


products = [
    Product(1001,"Iphone 17 Pro Max","Latest Iphone in the market", 150000.0,3)
]

@app.get("/")
def greet():
    return "Welcome to my new FastAPI Application !!!"

@app.get("/health")
def health():
    return "Application is healthy & running fine !!!"

@app.get("/products")
def getProducts():
    return products