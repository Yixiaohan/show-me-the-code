# -*- coding: utf-8 -*-
import mysql.connector

def storeInSql(filepath):
	file = open(filepath, "r")
	user = "root"
	passw = "yanghan98"
	database = "activate_code"
	conn = mysql.connector.connect(user = user, password = passw, database = database)
	cursor = conn.cursor()

	cursor.execute("SHOW TABLES;")
	tables = cursor.fetchall()
	existed = False
	for table in tables:
		if 'activate_code' in table:
			existed = True
	if not existed:
		cursor.execute('''
			CREATE TABLE activate_code (
			id INT NOT NULL AUTO_INCREMENT,
			code VARCHAR(20) NOT NULL,
			PRIMARY KEY (id)
			);
			''')
	for line in file.readlines():
		code = line.strip()
		print code
		cursor.execute("INSERT INTO activate_code (code) VALUES (%s);", [code])

	conn.commit()
	cursor.close()
	conn.close()




if __name__ == '__main__':
	filepath = "../0001/activate_code.txt"
	storeInSql(filepath)