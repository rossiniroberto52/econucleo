from fastapi import FastAPI
import sqlite3, datetime

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

@app.post("/create_new_request")
def create_request(name:str, cpf:str, age:int, book_id:int, address:str, return_day:str = ""):
    current_time = datetime.datetime.now()
    
    date_day = current_time.day
    date_month = current_time.month
    date_year = current_time.year
    date = f"{date_day+10}/{date_month}/{date_year}"
    
    if len(return_day) == 0:
        date_day + 10
        data = (name, cpf, age, book_id, date, address)
    else:
        data = (name, cpf, age, book_id, return_day, address)
    
    query = '''
        INSERT INTO tb_pedidos(T_NAME, T_CPF, N_AGE, N_ID_BOOKS, T_REC_DAY, T_ADDRESS)
        VALUES(?,?,?,?,?,?)
    '''
    return DataBaseARG(query, data)

@app.get("/get_all_request")
def get_all_request():
    query = "SELECT * FROM tb_pedidos"
    return DataBase(query)

@app.post("/update_request")
def update_request():
    pass