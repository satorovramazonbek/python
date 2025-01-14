import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)
print(todos[0])
#
# data = {
#     "president": {
#         "name": "Zaphad beeblebrex",
#         "species": "Betelgenian"
#     }
# }
#
# js_data = json.dumps(data, indent=4)
# with open("data_file.json", "w") as write_file:
#     write_file.write(js_data)
#
# py_data = json.loads(js_data)
# # print(py_data)
# with open("data_file.json", "r") as read_file:
#     data = json.load(read_file)
# print(data)
