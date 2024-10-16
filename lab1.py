user_name = input("Введите имя: ")
print("Привет, " + user_name + "!")

integer_var = 69
float_var = 3.14
short_text_var = "Hello World"
long_text_var = """Это саммый мучительный текст
Ведь я его писал 
в 5 часов ночи ;("""

print("integer_var:", type(integer_var))
print("float_var:", type(float_var))

print("long_text_var:", len(long_text_var))

upper_case_text = short_text_var.upper()
print("Текст в верхнем регистре:", upper_case_text)

substring = long_text_var[:29] 
print("Подстрока из long_text_var:", substring)

# a)
txt_a = "More results from text..."
substr = txt_a[4:12]
print("a) Подстрока:", substr)
print("a) Подстрока без пробелов:", substr.strip())

# b)
txt_b = "More results from text..."
print("b) Разделение текста на слова:", txt_b.split())

# c)
age = 36
txt_c = "My name is Mary, and I am {}"
print("c) Форматирование текста с использованием переменной age:", txt_c.format(age))
input("Press Enter to exit...")