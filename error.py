from sql_function import Sql_func
from other import Other


########################################### ПРОВЕРКА НА ОШИБКИ ##########################################
class Check_error:
	def __init__(self):
		self.sql_func = Sql_func()
		self.other = Other()

	# Проверка на правильность данных от пользователя
	def error_amount_data(self, game: str):
		if len(self.other.format_game(game)) == 3:
			return True
		return False

	# Проверка есть ли игра или нет
	def error_check_game(self, game: str):
		info = self.other.format_game(game)
		if self.sql_func.check_game(info[0], info[1], info[2]):
			return True
		return False
