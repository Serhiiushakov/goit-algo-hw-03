#Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе 
#генерувати набір унікальних випадкових чисел для таких лотерей.

import random

def input_function():
    min_number, max_number, quantity_number = 0, 0, 0 #створення параметрів функції

    while True: # Цикл на помилки
        try:
            if  min_number and min_number > 0: # мін
                pass
            else:
                min_number = int(input("Введіть міінімальне значення, яке більшео 0: "))
                continue
            if max_number and max_number < 1001:
                pass
            else:    
                max_number = int(input("Введіть максимальне зпнчення, яке менше 1000: "))
                continue
            if quantity_number: # кількість
                pass
            else:    
                quantity_number = int(input("Ведіть кількість цифр для вивведення: ")) 
                continue
            break
        except ValueError:
            print("Вибачте, введіть вірно число")
            continue
    return (min_number, max_number, quantity_number)

def get_numbers_ticket(min_number, max_number, quantity_number):
    number_list = []
    if min_number >= max_number or max_number - min_number < quantity_number: # пустий список
        return number_list
    
    while quantity_number > 0: # цикл поки 0
        random_number = random.randint(min_number, max_number) # рандом
        if random_number in number_list: # наповнюємо список
            continue
        else:
            number_list.append(random_number) 
            quantity_number -= 1
    return (number_list)
print(get_numbers_ticket(*input_function()))
