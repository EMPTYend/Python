from function import add_item, remove_item, display_items

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
