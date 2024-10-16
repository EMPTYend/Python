from lab6tarasov_module import Employee, HourlyEmployee, SalaryEmployee

# Создаем объекты с ручным вводом данных
print("Создание сотрудника:")
name = input("Введите имя: ")
phone = input("Введите телефон: ")
birthday = input("Введите дату рождения (в формате ДД.ММ.ГГГГ): ")
email = input("Введите email: ")
position = input("Введите должность: ")

emp1 = Employee(name, phone, birthday, email, position)

print("\nСоздание почасового сотрудника:")
name = input("Введите имя: ")
phone = input("Введите телефон: ")
birthday = input("Введите дату рождения (в формате ДД.ММ.ГГГГ): ")
email = input("Введите email: ")
position = input("Введите должность: ")
hours_worked = int(input("Введите количество отработанных часов: "))
hourly_rate = float(input("Введите почасовую ставку: "))

emp2 = HourlyEmployee(name, phone, birthday, email, position, hours_worked, hourly_rate)

print("\nСоздание сотрудника с фиксированной зарплатой:")
name = input("Введите имя: ")
phone = input("Введите телефон: ")
birthday = input("Введите дату рождения (в формате ДД.ММ.ГГГГ): ")
email = input("Введите email: ")
position = input("Введите должность: ")
monthly_salary = float(input("Введите фиксированную месячную зарплату: "))

emp3 = SalaryEmployee(name, phone, birthday, email, position, monthly_salary)

# Проверяем методы
print("\nРезультаты:")
print("Возраст сотрудника:", emp1.calculateAge())
print("Зарплата почасового сотрудника:", emp2.calculateSalary())
print("Зарплата сотрудника с фиксированной зарплатой:", emp3.calculateSalary())
