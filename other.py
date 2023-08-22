########################################### ПРОЧИЕ ФУНКЦИИ ##########################################
class Other:
	# Разбивает от пользовтеля на список
	def format_game(self, game: str):
		info = game.split()
		return info

	# Преобразует данные от бд
	def format_list_games(self, all_games: list):
		all_games_text = "\n".join([f"{i[0]} {i[1]} {i[2]}" for i in all_games])
		return all_games_text
