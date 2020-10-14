# здесь подключите библиотеку random и дайте ей краткое имя
import random as rand
answers = ['Норм.', 'Лучше всех :)', 'Ну так', 'Отличненько!', 'Ничего, жить буду']
def how_are_you():
    return rand.choice(answers) # напишите ваш код здесь
print(how_are_you())


import datetime as dt
start_time = dt.datetime(2011, 4, 17)  # дата выхода первой серии
final_time = dt.datetime(2019, 4, 15)  # впишите дату выхода последней серии
duration = final_time - start_time  # вычислите, сколько времени шёл сериал
print(duration)

# подключите библиотеку datetime под именем dt
import datetime as dt
start_moment = dt.datetime(2020, 9, 20)  # напишите код здесь
current_moment = dt.datetime(2020, 10, 14)  # напишите код здесь
total_time = current_moment - start_moment  # и здесь
print(total_time)
now = dt.datetime.utcnow()
period = dt.timedelta(hours=3)
moscow_moment = now + period
print(moscow_moment)  # будет напечатано текущее время в Москве
