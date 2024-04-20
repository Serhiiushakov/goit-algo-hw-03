import re

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
    "++972545379039",
]

def normalize_phone(num):
    pattern = r"\+?\d+" # Патерн для пошуку номерів, з "+" плюс 
    result = re.findall(pattern, num)
    new_result = "".join(result) # зєднуємо знайдені рядки
    if re.fullmatch(r"\+\d+", new_result): #  с "+38" нічого не робимо, все ок
        pass
    elif re.fullmatch(r"38\d+", new_result): # якщо, номер з "38" додати "+" перед номером
        new_result = "+" + new_result
    else: # всі інші випадки додаємо  "+38"
        new_result = "+38" + new_result
    return new_result

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
