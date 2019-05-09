import sqlite3

database_file = 'upload_result.db'

# IF NOT EXISTS 구문을 사용하실 경우 CREATE DATABASE 구문을 사용해 만들고자 하는 데이터베이스가  
# 이미 존재할 경우 발생할 수 있는 오류를 피할 수 있습니다.
create_query = "CREATE TABLE IF NOT EXISTS upload_result(date TEXT, result TEXT, path TEXT)"
with sqlite3.connect(database_file) as conn:
    c = conn.cursor()
    c.execute(create_query)