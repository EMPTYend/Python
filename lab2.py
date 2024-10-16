# Задание 1
my_list = [1, 2, 3, 4, 5]

print("первое значение:", my_list[0])
print("Второе значение:", my_list[2])

my_list[1] = 10

sliced_list = my_list[1:4]

my_list.append(6)
my_list.extend([7, 8])
my_list.pop(2)
print("Лист после:", my_list)

my_tuple = (10, 20, 30, 40, 50)

print("Вывод после my_tuple:", type(my_tuple))

print("Первое значение:", my_tuple[0])
print("последнее значение:", my_tuple[-1])

sliced_tuple = my_tuple[1:4]

sum_tuple = sum(my_tuple)
max_tuple = max(my_tuple)
min_tuple = min(my_tuple)
print("Sum, max, min:", sum_tuple, max_tuple, min_tuple)

my_set = {1, 2, 3, 3, 4, 5}

print("Вывод:", my_set)

my_set.add(6)
my_set.remove(2)
union_set = my_set.union({7, 8})
print("Обновленные знач:", union_set)

text_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
numeric_dict = {1: "один", 2: "два", 3: "три"}

print("Словарь:", text_dict)
print("Тоже самое но с цифрами:", numeric_dict)

print("Значение 'key2':", text_dict["key2"])
print("Тоже значение key 2:", numeric_dict[2])

text_dict.update({"key4": "value4"})
numeric_dict.pop(1)
print("Обновлённый словарь:", text_dict, numeric_dict)

my_str = "123"
converted_int = int(my_str)
print("конвертирование:", converted_int)

# Задание 2

numeric_list = [100, 200, 300]

text_list = ["A", "B", "C"]

info_product_1 = "{}: ${}".format(text_list[0], numeric_list[0])
info_product_2 = "{}: ${}".format(text_list[1], numeric_list[1])
info_product_3 = "{}: ${}".format(text_list[2], numeric_list[2])

print(info_product_1)
print(info_product_2)
print(info_product_3)

user_age_str = input("Возраст: ")
user_age = int(user_age_str)

future_age = user_age + 5

print("Через 5 лет тебе будет около {} миллионов лет.".format(future_age))

my_string = "Python programming"

if "python" in my_string.lower():
    print("Подстрока «python» есть ;)")
else:
    print("А тут нет подстроки «python» ;(")

# Проверка отсутствия подстроки
if "java" not in my_string.lower():
    print("Подстрока «java» отсутствует в нашем сознании ;(")
else:
    print("Подстрока «java» теперь доступна ;)")

input("Press Enter to exit...")