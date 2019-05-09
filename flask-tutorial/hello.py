
from flask import Flask, send_from_directory, request, json, redirect
import datetime

image_dir = "images"

app = Flask(__name__)

@app.route('/')
def hello_world():
	return send_from_directory(directory="",filename="index.html")

@app.route("/upload", methods=['POST'])
def updoad():
	image_file = request.files["file"]
	path = "{0}/{1}".format(image_dir, image_file.filename)
	image_file.save(path)
	history()
	return json.dumps({"path":path})

@app.route("/images/<name>")
def image(name):
	return send_from_directory(directory="image_dir", filename=name)
	
@app.route("/history")
def history():
	now = datetime.datetime.now()
	fw = open('/workspace/Tutorial1/history/%s.txt' %now, 'wt', encoding="utf-8")
	fw.write('업로드된 날짜 : %s' %now)
	fw.close()
	
	fr = open('/workspace/Tutorial1/history/%s.txt' %now, 'rt', encoding="utf-8")
	text = fr.read()
	print(text)
	fr.close()
	return

