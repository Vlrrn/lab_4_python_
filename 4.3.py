# Реализуйте базовый класс Car.
#   1. У класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
#      А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
#   2. Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
#   3. Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
#   4. Для классов TownCar и WorkCar переопределите метод show_speed.
#   При начении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

class Car:
    cars = []

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        Car.cars.append(self)

    def go(self):
        print("{} поехала".format(self.name))

    def stop(self):
        print("{} остановилась".format(self.name))

    def turn(self, direction):
        print("{} повернула {}".format(self.name, direction))

    def show_speed(self):
        print("Текущая скорость {} - {} км/ч".format(self.name, self.speed))


class TownCar(Car):
    def show_speed(self):
        print("Текущая скорость {} - {} км/ч".format(self.name, self.speed))
        if self.speed > 60:
            print("Нарушение {} скоростного режима!".format(self.name))


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print("Текущая скорость {} - {} км/ч".format(self.name, self.speed))
        if self.speed > 40:
            print("Нарушение {} скоростного режима!".format(self.name))


class PoliceCar(Car):
    pass


c1 = WorkCar(41, "красный", "name 1", False)
c1.go()
c1.show_speed()
c1.turn("налево")
c1.stop()
print()
c2 = SportCar(100, "синий", "name 2", False)
c2.go()
c2.show_speed()
c2.turn("направо")
print("Цвет {} - {}".format(c2.name, c2.color))
print()
c3 = TownCar(70, "жёлтый", "name 3", False)
c3.go()
c3.show_speed()
