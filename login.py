import sqlite3
from sign_up import sign_up

def login():
    
    TcNo=input("Tc No:")
    password=input("Şifreniz:")

    connect=sqlite3.connect("patient.db")
    cursor=connect.cursor()
    cursor.execute('SELECT * FROM patient WHERE TcNo=? AND password=? ',(TcNo,password))
    patient=cursor.fetchone()
    connect.close()

    if patient is not None:
        if patient[2]==TcNo:
            if patient[3]==password:
              print(f"Merhaba {patient[0]} {patient[1]}!.Giriş Başarılı.")
            else:
               print("Şifreniz hatalı.")
        else:
            print("Tc Kimlik No yanlış girildi.")
    else:
        print("Kayıt bulunamadı lütfen kayıt olunuz.")
        sign_up()