import re
import datetime

class Employee:
    def __init__(self, name, phone, birthday, email, specialty):
        self.__name = name
        self.__phone = phone
        self.__birthday = datetime.datetime.strptime(birthday, "%d.%m.%Y").date()
        self.__email = email
        self.__specialty = specialty
    
    def calculateAge(self):
        today = datetime.date.today()
        age = today.year - self.__birthday.year - ((today.month, today.day) < (self.__birthday.month, self.__birthday.day))
        return age
    
    def calculateSalary(self):
        pass

    
    # Getter и Setter для name
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        if re.match(r'^[a-zA-Z-]+$', name):
            self.__name = name
        else:
            print("Некорректное имя.")
    
    name = property(get_name, set_name)

    # Другой вариант с использованием декораторов
    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self, phone):
        if re.match(r'^\+373\d{7}$', phone):
            self.__phone = phone
        else:
            print("Некорректный номер телефона.")

    # Аналогично определяем getter и setter для остальных свойств


class HourlyEmployee(Employee):
    def __init__(self, name, phone, birthday, email, specialty, hours_worked, hourly_rate):
        super().__init__(name, phone, birthday, email, specialty)
        self.__hours_worked = hours_worked
        self.__hourly_rate = hourly_rate
    
    def calculateSalary(self):
        return self.__hours_worked * self.__hourly_rate


class SalaryEmployee(Employee):
    def __init__(self, name, phone, birthday, email, specialty, monthly_salary):
        super().__init__(name, phone, birthday, email, specialty)
        self.__monthly_salary = monthly_salary
    
    def calculateSalary(self):
        return self.__monthly_salary
