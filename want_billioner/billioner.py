import json

startstr = """
Kim milliarder bo'lishni istaydi o'ynigaa xush kelibsiz!
    Buyruqni tanlang:
    1 - o'ynash
    2 - reyting
    
    0 - dasturdan chiqish
"""
print(startstr)
# command = int(input())
# playername = input("O'yinchining ismini kiriting: ")

players = {
    "Ramazonbek": {
        "count": 0,
        "best_score": 0
    }
}

# player = json.dumps(players, indent=4)
# with open("players.json", "w") as write_file:
#     write_file.write(player)

with open("tests.json", "r") as read_file:
    tests = json.load(read_file)

for n in range(len(tests)):
    for i in range(4):
        if tests[n]["answers"][i]['isTrue'] == "true":
            print(tests[n]['answers'][i]['key'])
# print(tests[0]["answers"][1]['key'])
