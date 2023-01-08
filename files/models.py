import sqlite3 as sql 
import random

class User():
	def __init__(self, fileDB):
		self.fileDB = fileDB

	def createUser(self, username, senha, email, telephone):
		banco = db(self.fileDB)
		banco.insert(f"""
			INSERT INTO users (username, password, telephone, email, newsletter) VALUES ({username or ''},{senha or ''},{telephone or ''},{email or ''}, {username})
		""")
		banco.insert(f"INSERT INTO newsletter (name, author) VALUES ({username or ''}, {username or ''})")
		return "OK"

	def editUser(self, username, senha, email, telephone, usernameLast):
		banco = db(self.fileDB)
		titleNewsletter = banco.selectOne(f"SELECT newsletter FROM users WHERE = {usernameLast}")
		banco.update(f"UPDATE users SET username = {username or ''}, password = {senha or ''}, email = {email or ''}, {telephone or ''} WHERE username = {usernameLast}")
		banco.update(f"UPDATE newsletter SET author = {usernameLast}")
		return "OK"

	def deleteUser(self, username):
		banco = db(self.fileDB)
		if not username:
			return "Not Username"
		banco.update(f"DELETE FROM users WHERE username = {username}")
		return "OK"

	def userinfo(self, username):
		banco = db(self.fileDB)
		return banco.selectAll(f"SELECT * FROM users WHERE = {username}")

	def authUser(self, username, senha):
		banco = db(self.fileDB)
		try:
			passwordUser = banco.selectOne(f"SELECT password FROM users WHERE = {username}")
		except Exception as e:
			return "User Not Exists"

		if senha == passwordUser[0]:
			return "OK"

class Newsletter():
	def __init__(self, fileDB):
		self.fileDB = fileDB

	def editNewsletter(self, name, description):
		banco = db(self.fileDB)
		banco.update(f"UPDATE newsletter SET name = {name}, description = {description or ''}")
		return "OK"

class db():
	def __init__(self, file):
		self.file = file

	def selectAll(self, cmd):
		db = sql.connect(self.file)
		cursor = db.cursor()
		r = cursor.execute(cmd)
		fetch = r.fetchall()
		db.close()
		return fetch 

	def selectOne(self, cmd):
		db = sql.connect(self.file)
		cursor = db.cursor()
		r = cursor.execute(cmd)
		fetch = r.fetchone()
		db.close()
		return fetch 

	def insert(self, cmd):
		db = sql.connect(self.file)
		cursor = db.cursor()
		cursor.execute(cmd)
		db.commit()
		db.close()

	def update(self, cmd):
		db = sql.connect(self.file)
		cursor = db.cursor()
		cursor.execute(cmd)
		db.commit()
		db.close()	

