import re

def input_data():
    while True:
        surname = input("Введите фамилию сотрудника: ")
        if not re.match(r'^[a-zA-Z]+(?:-[a-zA-Z]+)?$', surname):
            print("Фамилия должна содержать только буквы и дефис, от 2 до 20 символов.")
            continue
        
        name = input("Введите имя сотрудника: ")
        if not re.match(r'^[a-zA-Z]+(?:-[a-zA-Z]+)?$', name):
            print("Имя должно содержать только буквы и дефис, от 2 до 20 символов.")
            continue
        
        department = input("Введите название отдела: ")
        if not re.match(r'^[a-zA-Z0-9 ]+$', department):
            print("Название отдела должно содержать буквы, цифры и пробелы.")
            continue
        
        children = input("Введите количество детей меньше 18 лет: ")
        if not children.isdigit() or not 0 <= int(children) <= 19:
            print("Количество детей должно быть целым числом от 0 до 19.")
            continue
        
        with open("data.txt", "a") as file:
            file.write(f"{surname}\t{name}\t{department}\t{children}\n")
        print("Данные успешно сохранены.")
        break

def view_data():
    total_children = 0
    with open("data.txt", "r") as file:
        for line in file:
            fields = line.strip().split("\t")
            print(f"Сотрудник: {fields[0]} {fields[1]}, отдел: {fields[2]}, детей: {fields[3]}")
            total_children += int(fields[3])
    print(f"Общее количество детей: {total_children}")

def childless_employees():
    childless_list = []
    with open("data.txt", "r") as file:
        for line in file:
            fields = line.strip().split("\t")
            if int(fields[3]) == 0:
                childless_list.append(f"{fields[0]} {fields[1]}")
    if childless_list:
        print("Список сотрудников без детей:")
        for employee in childless_list:
            print(employee)
    else:
        print("В компании нет сотрудников без детей.")

def main():
    while True:
        print("\nМеню:")
        print("1. Ввод данных о сотрудниках")
        print("2. Просмотр данных о сотрудниках")
        print("3. Вывод списка бездетных сотрудников")
        print("4. Выход")
        choice = input("Выберите опцию: ")

        if choice == "1":
            input_data()
        elif choice == "2":
            view_data()
        elif choice == "3":
            childless_employees()
        elif choice == "4":
            print("Программа завершена.")
            break
        else:
            print("Некорректный ввод. Пожалуйста, выберите опцию из меню.")

if __name__ == "__main__":
    main()
