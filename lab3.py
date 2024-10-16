# Задание 1
i = sum = 0
while i <= 4:
    sum += i
    i = i + 1
print(sum)

for char in 'PYTHON STRING':
    if char == ' ':
        break
    print(char, end='')
    if char == 'O':
        continue
    print('*', end='')

# Задание 2
user_input = input("Введите значение: ")
if user_input.isdigit():
    print("Вы ввели целое число.")
elif user_input.replace('.', '', 1).isdigit():
    print("Вы ввели вещественное число.")
else:
    print("Вы ввели текст.")

my_list = [1, 2, 3, 4, 5, 2, 3]
my_dict = {'apple': 3, 'banana': 2, 'orange': 5}

value_to_count_list = 2
count_list = my_list.count(value_to_count_list)
print(f"Значение {value_to_count_list} встречается в списке {count_list} раз(а).")

value_to_count_dict = 'banana'
count_dict = list(my_dict.values()).count(my_dict[value_to_count_dict])
print(f"Значение '{value_to_count_dict}' встречается в словаре {count_dict} раз(а).")

square = lambda x: x ** 2
print(f"Квадрат числа 5: {square(5)}")

# Задание 3
from functions import add_item, remove_item, display_items

shopping_list = []

while True:
    print("\nМеню:")
    print("1. Вывести список текущих товаров")
    print("2. Добавить товар в список")
    print("3. Удалить товар из списка")
    print("4. Выход")

    choice = input("Выберите опцию (1-4): ")

    if choice == '1':
        display_items(shopping_list)
    elif choice == '2':
        new_item = input("Введите товар для добавления: ")
        add_item(shopping_list, new_item)
    elif choice == '3':
        item_to_remove = input("Введите товар для удаления: ")
        remove_item(shopping_list, item_to_remove)
    elif choice == '4':
        print("Программа завершена.")
        break
    else:
        print("Неверный ввод. Пожалуйста, введите число от 1 до 4.")

input("Press Enter to exit...")