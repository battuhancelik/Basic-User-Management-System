import sqlite3
from random import SystemRandom
from string import digits

def ForgotPassword():
    choice=input("işleminizi Telefon numarasıyla mı yoksa email ile mi gerçekleştireceksiniz?(e/t) ")
    
    if choice=="t":
        TcNo=input("Tc No:")
        telephone=input("Cep Telefonu:")
        
        connect=sqlite3.connect("patient.db")
        cursor=connect.cursor()
        cursor.execute('SELECT * FROM patient WHERE TcNo=? AND telephone=? ',(TcNo,telephone))
        patient=cursor.fetchone()

        while True:
            vertificationCode="".join(SystemRandom().choice(digits) for i in range(6))
            print(f"Doğrulama kodu {telephone} nolu telefona gönderilmiştir.")
            print("Doğrulama kodunuz:",vertificationCode)
            confirmCode=input("Doğrulama kodu:")

            if confirmCode==vertificationCode:
                newPassword=input("Yeni şifreniz:")
                confirmPassword=input("Yeni şifre tekrar:")

                if newPassword==confirmPassword:
                    if newPassword!=patient[3]:
                        cursor.execute('UPDATE patient SET password=? WHERE TcNo=? AND telephone=?',(newPassword,TcNo,telephone))
                        connect.commit()
                        print("Şİfreniz başarıyla değiştirildi.")
                        break
                    else:
                        print("Yeni şifre, eski şifre ile aynı olamaz. Lütfen farklı bir şifre seçin.")
                else:
                    print("Girdiğiniz yeni şifreler uyuşmuyor.")
            else:
                print("Doğrulama kodu hatalı girildi.")
    
    elif choice=="e":
        TcNo=input("Tc No:")
        email=input("Email:")
        
        connect=sqlite3.connect("patient.db")
        cursor=connect.cursor()
        cursor.execute('SELECT * FROM patient WHERE TcNo=? AND email=? ',(TcNo,email))
        patient=cursor.fetchone()
 
        while True:
            vertificationCode="".join(SystemRandom().choice(digits) for i in range(6))
            print(f"Doğrulama kodu {email} adresine gönderilmiştir.")
            print("Doğrulama kodunuz:",vertificationCode)
            confirmCode=input("Doğrulama kodu:")

            if confirmCode==vertificationCode:
                newPassword=input("Yeni şifreniz:")
                confirmPassword=input("Yeni şifre tekrar:")

                if newPassword==confirmPassword:
                    if patient[3]!=newPassword:
                        cursor.execute('UPDATE patient SET password=? WHERE TcNo=? AND email=?',(newPassword,TcNo,email))
                        connect.commit()
                        print("Şİfreniz başarıyla değiştirildi.")
                        break
                    else:
                        print("Yeni şifre, eski şifre ile aynı olamaz. Lütfen farklı bir şifre seçin.")
                else:
                    print("Girdiğiniz yeni şifreler uyuşmuyor.")
            else:
                print("Doğrulama kodu hatalı girildi.")