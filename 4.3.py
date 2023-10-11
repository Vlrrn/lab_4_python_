# Реализуйте базовый класс Car.
#   1. У класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
#      А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
#   2. Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
#   3. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
#   4. Для классов TownCar и WorkCar переопределите метод show_speed.
#   При начении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car():
    speed = 0
    color = ''
    name = ''
    is_police = False
    cars = []

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        Car.cars.append(self)

    def go(self):
        print("----")

    def stop(self):
        print("||")

    def turn(self, direction):
        print("/", direction)

    def show_speed(self):
        print(self.speed)


class TownCar(Car):
    def tc_m(self):
        print("tc")

    def show_speed(self):
        if self.speed > 60:
            print("Нарушение! > 60")


class SportCar(Car):
    def sc_m(self):
        print("sc")


class WorkCar(Car):
    def wc_m(self):
        print("wc")

    def show_speed(self):
        if self.speed > 40:
            print("Нарушение! > 40")


class PoliceCar(Car):
    def pc_m(self):
        print("pc")


c1 = WorkCar(41, "red", "name 1", False)
c1.show_speed()
c2 = SportCar(20, "blue", "name 2", False)
c2.show_speed()
c2.turn("left")