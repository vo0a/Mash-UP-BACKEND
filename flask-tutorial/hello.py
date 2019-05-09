from flask import Flask, send_from_directory, request, json, redirect
import datetime

app = Flask(__name__)

@app.route('/')
def hello_world():
	return send_from_directory(directory="",filename="index.html")

@app.route("/upload", methods=['POST'])
def updoad():
	f = request.files["file"]
	path = "images/" + f.filename
	f.save(path)
	history()
	return json.dumps({"path":path})

@app.route("/images/<name>")
def image(name):
	return send_from_directory(directory="images", filename=name)
	
@app.route("/history")
def history():
	now = datetime.datetime.now()
	fw = open('/workspace/Tutorial1/history/%s.txt' %now, 'wt', encoding="utf-8")
	fw.write('���ε� �� �ð� : %s' %now)
	fw.close()
	
	fr = open('/workspace/Tutorial1/history/%s.txt' %now, 'rt', encoding="utf-8")
	text = fr.read()
	print(text)
	fr.close()
	return