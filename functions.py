
def add_item(shopping_list, item):
    shopping_list.append(item)
    print(f"Товар '{item}' добавлен в список.")

def remove_item(shopping_list, item):
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"Товар '{item}' удален из списка.")
    else:
        print(f"Товар '{item}' не найден в списке.")

def display_items(shopping_list):
    print("Текущий список товаров:")
    for i, item in enumerate(shopping_list, 1):
        print(f"{i}. {item}")
