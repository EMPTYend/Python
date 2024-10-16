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
input("Press Enter to exit...")