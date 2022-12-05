import json

with open('pliki/dane4.json', 'r') as f:
   data = json.load(f)

print(data['members'])
print(data['members'][2])
print(data['members'][2]['powers'])
print(data['members'][2]['powers'][3])

for i in data:
    print(i)

