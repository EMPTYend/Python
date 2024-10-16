greet_user = lambda name : print('Hello My Dear, ', name)
user_name = input("What is your name? ")
greet_user(user_name)

my_list = [(3, 11), (1, 7), (7, 8), (16, 88), (23, 15)]

sorted_list = sorted(my_list, key=lambda x: x[1])

print(sorted_list)
input("Press Enter to exit...")