def calc_stat(listened):  # от англ. calculate statistics, посчитать статистику
    T = 0
    for i in range (len (listened)):
        T+= int (listened[i])
    return (f'Вы прослушали {len(listened)} песен, общей продолжительностью {T//60} минут и {T%60} секунд.')  # напишите код функции calc_stat

print(calc_stat([193, 148, 210, 144, 174, 159, 163, 189, 230, 204]))
