# Создать класс Airline: Пункт назначения, Номер рейса, Тип самолета, Время вылета, Дни недели.
# Создать список объектов. Вывести:
#           a) список рейсов для заданного пункта назначения;
#           b) список рейсов для заданного дня недели
import colorama
from colorama import Fore, Style

colorama.init()


class Airline:
    l = []

    def __init__(self, destination, flight_number, airplane_type, departure_time, day):
        self.destination = destination
        self.flight_number = flight_number
        self.airplane_type = airplane_type
        self.departure_time = departure_time
        self.day = day
        Airline.l.append(self)

    def __str__(self):
        return "{} {} {} {} {}".format(self.destination, self.flight_number, self.airplane_type, self.departure_time,
                                       self.day)


def check_int(s):
    while True:
        try:
            c = int(input(s))
            return c
        except ValueError:
            print(Fore.RED + "\nВведите целое число!\n" + Style.RESET_ALL)


def check_input(s, goal: int):
    while True:
        in_ = (input(s)).capitalize()
        in_ = in_.replace(' ', '')
        for d in Airline.l:
            if goal == 1:
                if d.destination == in_:
                    return in_
            if goal == 2:
                if d.day == in_:
                    return in_
        print("Такого нет.")
        return


a1 = Airline("Minsk", 3, "civil", "15:25", "Mon")
a2 = Airline("Paris", 2, "civil", "10:00", "Sun")
a3 = Airline("Minsk", 6, "civil", "20:40", "Wed")
while True:
    print("""
            Выввести :
       1) По пункту назанчения
       2) По дню недели
       3) Все рейсы
       0) Выход """)
    while True:
        n = check_int("- ")
        if n < 0 or n > 4:
            print("Нет такого пункта. Повторите:")
        else:
            break
    print()
    if n == 1:
        message = "Введите пункт назначения: "
    elif n == 2:
        message = "Введите день недели: "
        # print(Airline.l[0])
    elif n == 3:
        print("Список рейсов:\n")
        for i in range(0, len(Airline.l)):
            print(Airline.l[i])
    else:
        print("""
                    ＞　    フ
                　　| 　_　 _|
                　 ／`ミ _x 彡
                　/　　　 　 |
                /　 ヽ　　 ﾉ
            ／￣|　　 |　|　|
            | (￣ヽ＿_ヽ_)_)
            ＼二つ
**********************************""")
        exit()
    if n == 1 or n == 2:
        in_ = check_input(message, n)
        for i in Airline.l:
            if n == 1:
                if i.destination == in_:
                    print(i)
            else:
                if i.day == in_:
                    print(i)
