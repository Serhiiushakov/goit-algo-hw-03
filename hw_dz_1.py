#Створіть функцію get_days_from_today(date), яка розраховує 
#кількість днів між заданою датою і поточною датою.

import datetime

def input_function():  # вводимо дату для обрахунку
    input_date = input(" Введіть будь ласка дату у форматі РРРР-ММ-ДД:")
    return input_date
    
def get_days_from_today(input_date_param):
    try:
        date = datetime.datetime.fromisoformat(input_date_param).date()
    except Exception as error:                         # ловимо не коректну дату ERROR
        print(error) 
        print("Вибачте, ви ввели не дату не коректно")
        return

    current_date = datetime.datetime.today().date()
    
    output_date = current_date.toordinal() - date.toordinal()  # використовуємо метод для обрахунку різниці між датами "toordinal"
    print(f"Між вибраною датою по відношеню до сьогоднішньої дати пройшло {output_date} днів")
    return output_date

input_date = input_function()
print(type(input_date))
get_days_from_today(input_date)
