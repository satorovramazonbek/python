# a = input()
# if a[0] == a[1] == a[2]:
#     print('sonlari bir xil')
# elif a[0]==a[1]or a[1]==a[2] or a[0]==a[2]:
#     print('sonlari teng')
# else:
#     print('sonlarini teng emas')

# a = int(input("Ob havoni kiriting"))
# if a<0:
#     print('Sovuq')
# elif a>=0 and a<=20:
#     print("Salqin")
# elif a>=21 and a<=30:
#     print("Iliq")
# else:
#     print("Issiq")

# sum = int(input("Xarid summasini kiriting"))
# if sum<50000:
#     print("Chegirma yo'q")
# elif sum>=50000 and sum<=100000:
#     print(f"Sizga 5% chegirma taqdim etildi siz {sum*0.95} so'm tolashingiz mumkin")
# else:
#     print(f"Sizga 10% chegirma taqdim etildi siz {sum*0.9} so'm to'lashingiz mumkin")

# login = input("Loginni so'rang")
# parol = input("Parolni kiriting")
# if login == 'admin'and parol=='12345':
#     print("Xush kelibsiz, admin!")
# else:
#     print("Login yoki parol xato")

# yosh = int(input("Yoshingizni kiriting: "))
# if yosh<13:
#     print("Siz bu filmni ko'ra olmaysiz")
# elif yosh>=13 and yosh <=17:
#     print("Siz bu filmni ota onangiz nazoratida ko'rishingiz mumkin")
# else :
#     print("Sizga bu fimlni ko'rishga ruxsat bor")

# choice = int(input("""Ovqat turini kiriting
# 1-'OSH', 2-'MASTAVA', 3- 'SHASHLIK'
# """))
# if choice == 1:
#     print("Siz Oshni tanladingiz ovqat 15daqiqada tayyor bo'ladi To'lashingiz kerak bo'lgan summa 35000 so'm")
# elif choice == 2:
#     print("Siz Mastavani tanladingiz ovqat 10daqiqada tayyor bo'ladi To'lashingiz kerak bo'lgan summa 25000m")
# elif choice == 3:
#     print("Siz Shashlikni tanladingiz ovqat 30daqiqada tayyor bo'ladi To'lashingiz kerak bo'lgan summa 50000 so'm")
# else:
#     print("Bundan kodli taom yo'q")

# email = input("Emailni kiriting: ")
# asss = email.find("@")
# print(asss)
# print(email.find('.'))
# if email.find('@') == -1 or email.find('.') == -1:
#     print('false')
# else:
#     print('True')

# score = int(input("Balingizni kiriting: "))
# if score <= 55:
#     print("Yaxshilab o'qi bahoying 2")
# elif score > 55 and score <= 69:
#     print("Harakat qil bahoting 3")
# if score >=70 and score<=85:
#     print("Narmalni harakat qil 4")
# if score >=86 and score<=100:
#     print("Devonacha o'qib qoyibsan 5 baho")

# sum = int(input("Kartayizdagi mablag'ni kiriting : "))
# yech = int(input("Yechmoqchi bo'lgan summayizni kiriting : "))
# answer = sum-yech
# if answer<0:
#     print("Hisobda yetarli mablag' mavjud emas!!! ")
# elif answer>=0 and yech<5000:
#     print("Yechiladigan minimal summa 5000 sum ")
# else:
#     print("Pul muvaffaqiyatli yechildi!!!")

# day = input("Hafta kunini kiriting : ")
# if day.lower() == 'shanba' or day.lower() == 'yakshanba':
#     print("Bugun dam olish kuni Mazza qib damini ol xodim ")
# else:
#     print("Bugun ish kuni Tur ishla yotmasdan")

mb = int(input("Oy davomida ishlatadigan trafik miqdorizni kiriting (GB) =  "))
if mb<=1:
    print("Do'stim sizga 'MINI' tarifi to'g'ri kelarkan")
if mb>1 and mb<=5:
    print("Do'stim sizga 'Standard' tarifi to'g'ri kelarkan")
if mb>5:
    print("Do'stim sizga 'UNLIMITED' tarifi to'g'ri kelarkan")