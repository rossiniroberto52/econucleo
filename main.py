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
    
def DataBaseARG(query:str, data:str):
    with sqlite3.connect("db.db3") as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute(query, data)
        log = cur.fetchall()
        return log

@app.get("/")
def root():
    return{"200"}

@app.get("/get_books")
def get_all_books():
    query = "SELECT * FROM tb_books"
    return DataBase(query)

@app.post("/create_book")
def create_new_book(name:str, author:str, release_year:str):
    data = (name, author, release_year)
    query = '''
            INSERT INTO tb_books(T_NAME, T_AUTHOR, T_RELEASE_YEAR)
            VALUES(?,?,?)
            '''
    return DataBaseARG(query, data)

@app.create("/create_new_reuquest")
def create_request(name:str,cpf:str,age:int,livro_id:int):
    pass

