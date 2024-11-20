# for i in range(0,5):   #i=0
#     print(i)
#
#
# print("/n")
# count =0
# while True:
#     print(count)   #0 1 2 3 4
#     count+=1


a=int(input("A ni kiriting "))
b=int(input("B ni kiriting "))
d = 0
# while True:
#     # d=a-b
#     if a-b<0:
#         print('bunday bulishi mumkin emas! ')
#         break
#     elif a-b==0:
#         print("bo'sh qolmaydi !")
#         break
#     elif a-b>b:
#         d=d-b
#     elif a-b<b:
#         print(b)
if a-b<0:
    print('bunday bulishi mumkin emas! ')
elif a-b==0:
    print("nol bo'sh joy yo'q")
else:       #a-b>0
    while a>=b:
        a=a-b
    if a==0:
        print('joy qolmadi')
    else:
        print(a)
