import sqlite3


########################################### РАБОТА С БД ##########################################
class Sql_func:
	def __init__(self):
		self.conn = sqlite3.connect("main.db")
		self.cur = self.conn.cursor()

	# Добавление новой игры
	def add_new_game(self, name: str, author: str, year: str):
		data = name, author, year
		self.cur.execute("INSERT INTO games VALUES(?, ?, ?)", data)
		self.conn.commit()

	# Проверка есть ли игра или нет
	def check_game(self, name: str, author: str, year: str):
		data = name, author, year
		result = self.cur.execute(f"SELECT * FROM games WHERE name = ? AND author = ? AND year = ?", data).fetchall()
		return bool(len(result))

	# Удаление игры
	def del_game(self, name: str, author: str, year: str):
		data = name, author, year
		self.cur.execute('''DELETE FROM games WHERE name = ? AND author = ? AND year = ?''', data)
		self.conn.commit()

	# Создание таблицы, если нет
	def create_dbx(self):
		self.cur.execute(
			'''CREATE TABLE IF NOT EXISTS games(name TEXT, author TEXT, year TEXT);''')
		self.conn.commit()

	# Получение всех игр
	def get_all_games(self):
		result = self.cur.execute(f"SELECT * FROM games").fetchall()
		return result

	# Изменение названия игры
	def upd_name(self, new_name: str, name: str, author: str, year: str):
		data = new_name, name, author, year
		self.cur.execute(
			'''UPDATE games SET name = ? WHERE name = ? AND author = ? AND year = ?''', data)
		self.conn.commit()

	# Изменение автора игры
	def upd_author(self, new_author: str, name: str, author: str, year: str):
		data = new_author, name, author, year
		self.cur.execute(
			'''UPDATE games SET author = ? WHERE name = ? AND author = ? AND year = ?''', data)
		self.conn.commit()

	# Изменение года выпуска игры
	def upd_year(self, new_year: str, name: str, author: str, year: str):
		data = new_year, name, author, year
		self.cur.execute(
			'''UPDATE games SET year = ? WHERE name = ? AND author = ? AND year = ?''', data)
		self.conn.commit()

	# Поиск игры по параметрам
	def search_games(self, parameter: str, value: str):
		result = self.cur.execute(f"SELECT * FROM games WHERE {parameter} = {value}").fetchall()
		return result
