
import json
import os
import random


def secret_number_generator():
    """Замыкание для генерации случайного числа"""
    def generate():
        return random.randint(1, 100)
    return generate


class GuessNumberGame:
    def __init__(self, secret_number=None, attempts=0, result=None):
        self.secret_number = secret_number or secret_number_generator()()
        self.attempts = attempts
        self.result = result

    def guess(self, number):
        """Проверка догадки"""
        self.attempts += 1
        if number < self.secret_number:
            print("Загаданное число больше!")
        elif number > self.secret_number:
            print("Загаданное число меньше!")
        else:
            print(f"Поздравляю! Вы угадали число {self.secret_number} за {self.attempts} попыток!")
            self.result = "Победа"
            return True
        return False

    def save_progress(self, filename="game_data.json"):
        """Сохранение состояния игры в JSON"""
        data = {
            "secret_number": self.secret_number,
            "attempts": self.attempts,
            "result": self.result
        }
        with open(filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
        print("Игра сохранена.")

    @staticmethod
    def load_progress(filename="game_data.json"):
        """Загрузка сохранённой игры"""
        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as file:
                data = json.load(file)
                print("Предыдущая игра загружена.")
                return GuessNumberGame(**data)
        else:
            print("Нет сохранённой игры. Начинаем новую.")
            return GuessNumberGame()


def main():
    game = GuessNumberGame.load_progress()

    print("Добро пожаловать в игру 'Угадай число'! (число от 1 до 100)")

    while True:
        try:
            user_input = input("Введите число (или 'exit' для выхода): ")
            if user_input.lower() == "exit":
                game.save_progress()
                print("Выход из игры. Прогресс сохранён.")
                break

            guess_number = int(user_input)
            if game.guess(guess_number):
                game.save_progress()
                break

        except ValueError:
            print("Пожалуйста, введите корректное число.")


if __name__ == "__main__":
    main()
