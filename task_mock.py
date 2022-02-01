import os


class Settings:
    def __init__(self):
        self.file = os.environ.get('FILE_WITH_SETTINGS')


def func_in_project():
    sett = Settings()
    if sett.file:
        with open(sett.file) as f:
            text = f.read()
            print(text)


if __name__ == '__main__':
    #  Нам нужно замокать вызов функции func_in_project так, чтобы вместо пути к файлу из переменной окружения
    #  Передался путь к файлу mock.txt, который находится в этой же директории.
    pass


