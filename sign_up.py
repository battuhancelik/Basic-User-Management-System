from database_connection import insert_user

def sign_up():
    TcNo=input("Tc No:")
    name=input("Adınız:")
    surname=input("Soyadınız:")
    gender=input("Cinsiyetiniz:")
    birthday=input("Doğum Tarihi(gün/ay/yıl):")
    telephone=input("Cep telefonu:")
    choose=input("Emailiniz varmı?(e/h):")
    
    if choose=="e":
        email=input("Email:")
        password=input("Şifreniz:")
        insert_user(TcNo,name,surname,password,telephone,email,gender,birthday)
        print("Kaydınız başarıyla oluşturuldu.")
    else:
        password=input("Şifreniz:")
        email=""
        insert_user(TcNo,name,surname,password,telephone,email,gender,birthday)
        print("Kaydınız başarıyla oluşturuldu.")
    
    



