# Создать class Human. Определить у него атрибуты имя и год рождения. Прописать 2 метода.
# Первый метод: выводит на экран имя и возраст ,
# второй метод : проверяет является ли человек совершеннолетним
import colorama
from colorama import Fore, Style
colorama.init()


class Human:
    name = ''
    year = 0

    def __init__(self, name, year):
        self.age = 2023 - year
        self.name = name
        self.year = year

    def method_1(self):
        print("Имя - ", self.name, "\nВозраст - ", self.age)

    def method_2(self):
        if self.age >= 18:
            print(self.name, "cовершеннолетний.")
        else:
            print(self.name, "несовершеннолетний.")


def check_int(s):
    while True:
        try:
            c = int(input(s))
            if 1900 < c < 2023:
                return c
            else:
                print("??!!")
                continue
        except ValueError:
            print(Fore.RED + "\nВведите целое число!\n" + Style.RESET_ALL)


print(Fore.CYAN + "\n", " " * 8, "Задание 1\n" + Style.RESET_ALL)
human = Human(input("Введите имя: "), check_int("Введите год рождения: "))
print()
human.method_1()
human.method_2()