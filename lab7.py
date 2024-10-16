import datetime
import re
import calendar
import math
# Задание 1: Рассчитать возраст в днях
def calculate_age_in_days():
    year_of_birth = int(input("Введите год рождения (YYYY): "))
    month_of_birth = int(input("Введите месяц рождения (MM): "))
    day_of_birth = int(input("Введите день рождения (DD): "))

    birth_date = datetime.date(year_of_birth, month_of_birth, day_of_birth)
    current_date = datetime.date.today()
    age_in_days = (current_date - birth_date).days

    print("Ваш возраст в днях:", age_in_days)

calculate_age_in_days()
# Задание 2: Определение дня недели для определенной даты
def determine_day_of_week():
    year = int(input("Введите год: "))
    month = int(input("Введите месяц: "))
    day = int(input("Введите день: "))

    day_number = calendar.weekday(year, month, day)
    day_name = calendar.day_name[day_number]

    print("День недели:", day_name)

determine_day_of_week()
# Задание 3: Расчет времени падения объекта
def calculate_fall_time():
    height = float(input("Введите высоту падения объекта (в метрах): "))
    g = 9.8  # ускорение свободного падения на поверхности Земли

    if math.isnan(height) or height <= 0:
        print("Высота должна быть числом больше нуля.")
        return

    time = math.sqrt(2 * height / g)
    print("Время падения объекта:", round(time, 2), "секунд")

calculate_fall_time()