import random    # імпортуємо рандом

def get_numbers_ticket(min, max, quantity): # функція, яка приймає 3 параметра

    #Перевіряємо чи коректні числа введені на вхід параметрів
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1) or min > max:
        return []   # Повертаємо пустий список, якщо параметри не коректно вибрані

    # Генеруємо випадкові та  унікальні числа
    result = random.sample(range(min, max + 1), quantity)

    # Повертаємо відсортований список чисел
    return sorted(result)

# Приклад використання із Конспекту д/з:
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
