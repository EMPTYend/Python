def calculate_ideal_weight(height, age, gender):
    if gender == 'М': 
        ideal_weight = height - 100 - ((height - 150) / 4 + (age - 20) / 4)
    elif gender == 'Ж':
        ideal_weight = height - 100 - ((height - 150) / 2.5 + (age - 20) / 6)
    else:
        return "Некорректно указан пол. Используйте 'М' или 'Ж'."
    
    return ideal_weight 

def weight_recommendation(actual_weight, ideal_weight):
    if actual_weight < ideal_weight:
        recommendation = "Вам нужно набрать вес."
    elif actual_weight > ideal_weight:
        recommendation = "Вам нужно снизить вес."
    else:
        recommendation = "Ваш вес идеален!"
    
    return recommendation

def main():
    gender = input("Введите ваш пол (М или Ж): ")
    height = int(input("Введите ваш рост в см: "))
    age = int(input("Введите ваш возраст в годах: "))
    actual_weight = float(input("Введите ваш текущий вес в кг: "))

    ideal_weight = calculate_ideal_weight(height, age, gender)
    if isinstance(ideal_weight, str):
        print(ideal_weight)
    else:
        print("Ваш идеальный вес: {:.2f} кг".format(ideal_weight))
        recommendation = weight_recommendation(actual_weight, ideal_weight)
        print(recommendation)

if __name__ == "__main__":
    main()
