import sqlite3
from random import SystemRandom
from string import ascii_letters

def update_info(name,surname):
    connect=sqlite3.connect("patient.db")
    cursor=connect.cursor()
    cursor.execute('SELECT * FROM patient WHERE name=? AND surname=?',(name,surname))
    patient=cursor.fetchone()  

    if patient is not None:
        while True:
            print("1- Telefon numara güncelleme\n2- Email güncelleme\n3- Password güncelleme")
            choose=input("Ne güncellemek istiyorsunuz: ")
            
            if choose=="1":
                newTelNumber=input("Yeni Telefon numarası:")
                code="".join(SystemRandom().choice(ascii_letters) for i in range(4))
                print("Doğrulama kodu:",code)
                confirm_code=input("Doğrulama kodu:")
                if code==confirm_code:
                    cursor.execute('UPDATE patient SET telephone=? WHERE name=? AND surname=?',(newTelNumber,name,surname))
                    connect.commit()
                    print("Telefon numaranız değiştirildi.")
                    break
                else:
                    print("Kod yanlış girildi.")
            
            elif choose=="2":
                newEmail=input("Yeni email:")
                code="".join(SystemRandom().choice(ascii_letters) for i in range(4))
                print("Doğrulama kodu:",code)
                confirm_code=input("Doğrulama kodu:")
                if code==confirm_code:
                    cursor.execute('UPDATE patient SET email=? WHERE name=? AND surname=?',(newEmail,name,surname))
                    connect.commit()
                    print("Email adresiniz değiştirildi.")
                    break
                else:
                    print("Kod yanlış girildi.")
            
            elif choose=="3":
                newPassword=input("Yeni Şifre:")
                code="".join(SystemRandom().choice(ascii_letters) for i in range(4))
                print("Doğrulama kodu:",code)
                confirm_code=input("Doğrulama kodu:")
                if code==confirm_code:
                    cursor.execute('UPDATE patient SET password=? WHERE name=? AND surname=?',(newPassword,name,surname))
                    connect.commit()
                    print("Şifreniz değiştirildi.")
                    break
                else:
                    print("Kod yanlış girildi.")
    else:
        print("Kullanıcı bulunamadı")