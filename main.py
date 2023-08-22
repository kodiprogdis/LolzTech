import colorama
from sql_function import Sql_func
from commands import Lobby


# Главная функция, которая запускает все
def start():
	sql_func = Sql_func()
	sql_func.create_dbx()
	print(colorama.Fore.RED + "Добро пожаловать в систему управления базой данных игр! Ниже команды:")
	lobby = Lobby()
	lobby.lobby()


# ЗАПУСК ФАЙЛА
if __name__ == "__main__":
	start()  # Запускаемая функция
