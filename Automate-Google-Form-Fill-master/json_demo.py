import json

user_details = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(user_details)

print(y['age'])