from sign_up import sign_up
from login import login
from password_management import ForgotPassword
from update_info import update_info
from delete_user import delete_user

while True:
    while True:
        print("1- Üye ol\n2- Giriş yap\n3- Şifremi unuttum\n4- Bilgileri güncelleme\n5- Kayıt Sil\n6- Çıkış")
        secim=input("Seçiminiz:")

        if secim=="1":
            sign_up()
            break
        elif secim=="2":
            login()
            break
        elif secim=="3":
            ForgotPassword()
            break
        elif secim=="4":
            name=input("isim:")
            surname=input("soyisim:")
            update_info(name,surname)
            break
        elif secim=="5":
            name=input("isim:")
            surname=input("soyisim:")
            delete_user(name,surname)
            break
        elif secim=="6":
            print("Çıkış yapıldı.")
            break
        else:
            print("Yanlış Seçim.Lütfen 1,2,3,4,5 veya 6'yı seçiniz.")