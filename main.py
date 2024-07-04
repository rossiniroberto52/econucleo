from fastapi import FastAPI
import sqlite3

app = FastAPI()

def DataBase(query:str):
    with sqlite3.connect("db.db3") as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(query)
        data = cur.fetchall()
        return data

@app.get("/")
def root():
    return{"200"}

@app.get("/get_books")
def get_all_books():
    query = "SELECT * FROM tb_books"
    return DataBase(query)

