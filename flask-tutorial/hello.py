from flask import Flask, send_from_directory, request, json, redirect
import datetime, sqlite3


image_dir = "images"

#있으면 해당 파일 오픈, 없으면 새 파일 생성
database_file = 'upload_result.db' 

app = Flask(__name__)

def write_log(database_file, result, path):
	try:
		# SQLite DB 연결
		con = sqlite3.connect(database_file)
		
		# Connection 으로부터 Cursor 생성
		cur = con.cursor()
		
		# SQL 쿼리 실행
		cur.execute("INSERT INTO upload_result(date, result, path) VALUES (?,?,?)", \
			(datetime.datetime.now(), result, path))
		con.commit()
	except:
		con.rollback()
	finally:
		con.close()
		
@app.route('/')
def hello_world():
	return send_from_directory(directory="",filename="index.html")

@app.route("/upload", methods=['POST'])
def upload():
	if "file" not in request.files:
		result = "Cannot find file"
		write_log(result, None)
		return "", 400
	
	image_file = request.files["file"]
	
	if image_file.filename == "":
		result = "File name is empty"
		write_log(result, None)
		return "", 400
	
	path = "{0}/{1}".format(image_dir, image_file.filename)
	image_file.save(path)
	
	write_log(database_file, "Success", path)
	return json.dumps({"path":path}), 200

@app.route("/images/<name>")
def image(name):
	return send_from_directory(directory="image_dir", filename=name)
