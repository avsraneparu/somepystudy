import json
with open('data.json', 'r') as data:
    m=json.load(data)
for key, value in m.items():
        print(key, value)
print(m['requests'])