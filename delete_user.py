import sqlite3

def delete_user(name,surname):
    connect=sqlite3.connect("patient.db")
    cursor=connect.cursor()
    cursor.execute('SELECT * FROM patient WHERE name=? AND surname=?',(name,surname))
    patient=cursor.fetchone()

    if patient is not None:
        _,_,TcNo,Password,Gender,Birthday,Telephone,Email=patient
        cursor.execute('DELETE FROM patient WHERE name=? AND surname=?',(name,surname))
        connect.commit()
        print("Kaydınız başarıyla silinmiştir.")
    else:
        print("Bu isim ve soyisimde bir kayıt yok.")