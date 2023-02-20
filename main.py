from flask import Flask
import json
from untils import data

app = Flask(__name__)
@app.route("/")
def page_index(): #home page
	return f'<pre>\n{data[1]["name"]}\n{data[1]["position"]}\n{data[1]["skills"]}\n \n{data[2]["name"]}\n{data[2]["position"]}\n{data[2]["skills"]}\n \n{data[3]["name"]}\n{data[3]["position"]}\n{data[3]["skills"]}\n \n{data[4]["name"]}\n{data[4]["position"]}\n{data[4]["skills"]}\n \n{data[5]["name"]}\n{data[5]["position"]}\n{data[5]["skills"]}\n \n{data[6]["name"]}\n{data[6]["position"]}\n{data[6]["skills"]}\n{data[7]["name"]}\n{data[7]["position"]}\n{data[7]["skills"]}<pre>'
	
@app.route("/candidate/<int:id>")

def id_search(id): #search by id
	return f'<img src="{data[id]["picture"]}">\n \n<pre>{data[id]["name"]}\n{data[id]["position"]}\n{data[id]["skills"]}<pre>'


@app.route("/skill/<skill>")
def skill_search(skill):
	str_candidate = ""
	for candidate in data.values():
		candidate_skills = candidate["skills"].split(" ,")
		for x in candidate_skills:
			x = x.lower()

			if skill in x:
				str_candidate += f'{candidate["name"]} <br>{candidate["position"]}<br> {candidate["skills"]}<br><br>'
		str_candidate += " "
	return str_candidate


app.run()
