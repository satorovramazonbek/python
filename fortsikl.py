# pochtalar=['user1@gmail.com',"user2yahoo.com","user3@outlook.com"]
# for pochta in pochtalar:
#     if pochta.find('@')==-1:
#         print(f"noto'g'ri email: {pochta}")

# passw = ["password123", "Qwerty!", "admin", "StrongPass1!"]
# for p in passw:
#     if len(p) < 8:
#         print("Parol juda qisqa", p)
#     elif p.isalnum() != 1 :
#         print('Belgilardan foydalanmang',p)
#     else:
#         print("Parol qabul qilindi!",p)

# infor = [20, 22, 19, 24, 25, 23, 21]
# p=0
# for inf in infor:
#     p+=inf
#     if p>=22:
#         print('Iliq kun')
#     else:
#         print("Salqin kun")
# print(p/len(infor))

# taom = ["OSH","Shashlik", "Manti", "Lag'mon"]
# tam=input("Taom turini kiriting\n")
# count =0
# for ta in taom:
#     if tam.lower() !=ta.lower():
#         count =1
#     else:
#         print("taomingiz qabul qilindi")
#         count=0
#         break
# if count==1:
#     print("Bizda bunday ovqat yo'q")

# yoshlar = [16, 21, 17, 30, 25]
# for yosh in yoshlar:
#     if yosh<18:
#         print("Yosh chegarasi yetmagan" ,yosh)
#     else:
#         print("Xush kelibsiz",yosh)

# xabarlar={"Yangi xabar", "Batareya past", "Yangilanish mavjud"}
# for xabar in xabarlar:
#     if xabar.lower() == "batareya past":
#         print("Telefoningizni quvvatlang")
#         break
#     else: continue

fayllar=["kitob.jpg", "ko_jiguli.mp3", "tabiat.jpg", "malohat.mp3","iphone16.jpg"]
musiqalar=[]
rasmlar=[]
for fayl in fayllar:
    if fayl.find('.jpg')!=-1:
        rasmlar.append(fayl)
    elif fayl.find('.mp3')!=-1:
        musiqalar.append(fayl)
print(rasmlar)