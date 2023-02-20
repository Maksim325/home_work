import json


with open('db.json', encoding='utf-8') as f:
   text = json.load(f)
data = {}
#print(text)
for i in text:
	data[int(i["id"])] = i
	#print(i)
	#data2[i["id"]] = i.pop('id') 