import sqlite3
#veritabanı oluşturma

def create_database():
    connect=sqlite3.connect("patient.db")
    cursor=connect.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS patient
    (Name TEXT,Surname TEXT,TcNo TEXT,Password Text,Gender TEXT,Birthday TEXT,Telephone TEXT,Email TEXT)''')
    connect.commit()
    connect.close()

#veritabanına veri ekleme
def insert_user(TcNo,name,surname,password,telephone,email,gender,birthday):
    connect=sqlite3.connect("patient.db")
    cursor=connect.cursor()
    cursor.execute('INSERT INTO patient (TcNo,name,surname,password,telephone,email,gender,birthday) VALUES (?,?,?,?,?,?,?,?)',(TcNo,name,surname,password,telephone,email,gender,birthday)) 
    connect.commit()
    connect.close()  