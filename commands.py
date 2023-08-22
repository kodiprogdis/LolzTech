import colorama
from error import Check_error
from other import Other
from sql_function import Sql_func


########################################### ГЛАВНОЕ МЕНЮ ##########################################
class Lobby:
	def lobby(self):
		command = input(colorama.Fore.LIGHTYELLOW_EX + '''Добавить игру - add_game | Поиск игры - search_game
Удалить игру - del_game | Редактировать данные о игре - edit_game
Вывод списка всех игр - list_games

Что бы покинуть игру введи другой любой текст.
''')
		games = Games()
		if command == "add_game":
			games.add_game()
		elif command == "search_game":
			games.search_game()
		elif command == "del_game":
			games.del_game()
		elif command == "edit_game":
			games.edit_game()
		elif command == "list_games":
			games.list_games()
		else:
			print(colorama.Fore.RED + "Пока-пока!")


########################################### ВСЕ КОМАНДЫ ##########################################
class Games:
	def __init__(self):
		self.error_check = Check_error()
		self.sql_func = Sql_func()
		self.other = Other()
		self.lobby = Lobby()

	# Добавить игру
	def add_game(self):
		game = input("Введи [название] [издатель] [год издания].\nПример: lolz kodi 2023\n")
		if self.error_check.error_amount_data(game):
			if not self.error_check.error_check_game(game):
				info_game = self.other.format_game(game)
				self.sql_func.add_new_game(info_game[0], info_game[1], info_game[2])
				print("Игра успешно добавлена!")
				self.lobby.lobby()
				return
			print("Произошла ошибка, кажется, игра уже добавлена. \nВы возвращены в меню!")
			self.lobby.lobby()
		print("Произошла ошибка, кажется, вы не указали досточное количество данных. \nВы возвращены в меню!")
		self.lobby.lobby()

	# Удалить игру
	def del_game(self):
		game = input("Введи [название] [издатель] [год издания] игры, которую хочешь удалить.\nПример: lolz kodi 2023\n")
		if self.error_check.error_amount_data(game):
			if self.error_check.error_check_game(game):
				info_game = self.other.format_game(game)
				self.sql_func.del_game(info_game[0], info_game[1], info_game[2])
				print("Игра успешно удалена!")
				self.lobby.lobby()
				return
			print("Игра не была найдена!")
			self.lobby.lobby()
		print("Произошла ошибка, кажется, вы не указали досточное количество данных. \nВы возвращены в меню!")
		self.lobby.lobby()

	# Просмотр всех игр
	def list_games(self):
		print(self.other.format_list_games(self.sql_func.get_all_games()))
		self.lobby.lobby()

	# Редактирование игры
	def edit_game(self):
		game = input("Введи [название] [издатель] [год издания] игры, у которой ты хочешь изменить.\nПример: lolz kodi 2023")
		if self.error_check.error_amount_data(game):
			if self.error_check.error_check_game(game):
				parameter = input("""Введи что ты хочешь изменить:
Название - name
Автор - author
Год - year
Вернуться назад - back\n""")
				info_game = self.other.format_game(game)
				if parameter == "name":
					new_info = input("Введи новое значение\n")
					self.sql_func.upd_name(new_info, info_game[0], info_game[1], info_game[2])
					self.lobby.lobby()
				elif parameter == "author":
					new_info = input("Введи новое значение\n")
					self.sql_func.upd_author(new_info, info_game[0], info_game[1], info_game[2])
					self.lobby.lobby()
				elif parameter == "year":
					new_info = input("Введи новое значение\n")
					self.sql_func.upd_year(new_info, info_game[0], info_game[1], info_game[2])
					self.lobby.lobby()
				elif parameter == "back":
					self.lobby.lobby()
				else:
					print("Параметр не найден!")
					self.lobby.lobby()
			print("Игра не была найдена!")
			self.lobby.lobby()
		print("Произошла ошибка, кажется, вы не указали досточное количество данных. \nВы возвращены в меню!")
		self.lobby.lobby()

	# Поиск игры
	def search_game(self):
		parameter = input("""По которому параметру будешь искать:
Название - name
Автор - author
Год - year
Вернуться назад - back\n""")
		if parameter == "name" or parameter == "year" or parameter == "author":
			value = input("Введи значение\n")
			results_search = self.sql_func.search_games(parameter, value)
			if len(results_search) != 0:
				print(self.other.format_list_games(results_search))
			else:
				print("Ни одна игра не найдена!")
			self.lobby.lobby()
		elif parameter == "back":
			self.lobby.lobby()
		else:
			print("Параметр не найден!")
			self.lobby.lobby()
