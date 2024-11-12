g = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
listgma = f"""
        {g[0]} - {g[1]} - {g[2]}
        ----------
        {g[3]} - {g[4]} - {g[5]}
        ----------
        {g[6]} - {g[7]} - {g[8]}
"""
print(listgma)
count = 2
while True:
    x = int(input("X= "))
    while g[x - 1] == "X" or g[x - 1] == "O":
        print("BU katak bo'sh emas. Qayta kiriting: ")
        x = int(input("X= "))
    g[x - 1] = 'X'
    print(f"""
        {g[0]} - {g[1]} - {g[2]}
        ----------
        {g[3]} - {g[4]} - {g[5]}
        ----------
        {g[6]} - {g[7]} - {g[8]}
""")
    if g[0] == g[1] and g[1] == g[2] or g[0] == g[3] and g[3] == g[6] or g[0] == g[4] and g[4] == g[8] or g[1] == g[
        4] and g[4] == g[7] or g[2] == g[5] and g[5] == g[8] or g[2] == g[4] and g[4] == g[6] or g[3] == g[4] and g[
        4] == g[5] or g[6] == g[7] and g[7] == g[8]:
        print('X yutdi tamom buldi uyin')
        break

    o = int(input("O uchun sonni kiriting: "))
    while g[o - 1] == "X" or g[o - 1] == "O":
        print("BU katak bo'sh emas. Qayta kiriting: ")
        o = int(input("O= "))
    g[o - 1] = 'O'
    print(f"""
        {g[0]} - {g[1]} - {g[2]}
        ----------
        {g[3]} - {g[4]} - {g[5]}
        ----------
        {g[6]} - {g[7]} - {g[8]}
""")

    if g[0] == g[1] and g[1] == g[2] or g[0] == g[3] and g[3] == g[6] or g[0] == g[4] and g[4] == g[8] or g[1] == g[
        4] and g[4] == g[7] or g[2] == g[5] and g[5] == g[8] or g[2] == g[4] and g[4] == g[6] or g[3] == g[4] and g[
        4] == g[5] or g[6] == g[7] and g[7] == g[8]:
        print('O yutdi tamom buldi uyin')
        break
