import ru_local as ru
wnted_priod = int(input('Введите количество месяцев, на котоорые вы хотите взять кредит: '))
wnted_percent = float(input('Введите желаемый процент: '))
begin_sum = float(input('Введите начальную сумму вклада: '))

percent = [11.5, 13.5, 14, 14.09, 13.8, 15, 11.5, 16, 16, 12.5]
period = [24, 12, 12, 6, 36, 3, 36, 6, 36, 12]

sum_of_priod = []


def deposit_sum(cash, percnt, time):
    for i in range(time):
        sum_of_priod.append(cash * (percnt / 100))
        cash += cash*(percnt/100)
    print('Сумма =', cash)
    print('Суммы в каждый месяц:', sum_of_priod)

#допустим, что depos_name - подходящий нам вклад


depos_name = 1

match depos_name:
    case 1:
        description = ru.TINKOFF_3
        print(ru.TINKOFF_3)
    case 2:
        description = ru.TINKOFF_12
        print(ru.TINKOFF_12)
    case 3:
        description = ru.TINKOFF_24
        print(ru.TINKOFF_24)
    case 4:
        description = ru.SBERBANK_12
        print(ru.SBERBANK_12)
    case 5:
        description = ru.VTB_6
        print(ru.VTB_6)
    case 6:
        description = ru.VTB_12
        print(ru.VTB_12)
    case 7:
        description = ru.ALFABANK_24
        print(ru.ALFABANK_24)
    case 8:
        description = ru.ALFABANK_36
        print(ru.ALFABANK_36)
    case 9:
        description = ru.LEVOBEREZHNY_12
        print(ru.LEVOBEREZHNY_12)
    case 10:
        description = ru.LEVOBEREZHNY_36
        print(ru.LEVOBEREZHNY_36)


#логическая функция на проверку соответствя
def check_exists_period(period, wnted_priod):   #первичный вариант, найду полегче решение поменяю функцию
    try:
        period.index(wnted_priod)
        return True
    except:
        return False


def check_exists_percent(percent, wnted_percent):
    try:
        percent.index(wnted_percent)
        return True
    except:
        return False


'''
if depos_name == '11.5% на 24мес - Тинькофф':
    deposit_sum(begin_sum, percent[0], period[0])
elif depos_name == '13.5% на 12мес - Тинькофф':
    deposit_sum(begin_sum, percent[1], period[1])
elif depos_name == '14% на 12мес - Сбер':
    deposit_sum(begin_sum, percent[2], period[2])
elif depos_name == '14.09% на 6мес - ВТБ':
    deposit_sum(begin_sum, percent[3], period[3])
elif depos_name == '14.75% на 36мес - АльфаБанк':
    deposit_sum(begin_sum, percent[4], period[4])
elif depos_name == '15% на 3мес- Тинькофф':
    deposit_sum(begin_sum, percent[5], period[5])
elif depos_name == '15.25% на 36мес - БанкЛевобережный':
    deposit_sum(begin_sum, percent[6], period[6])
elif depos_name == '16% на 6мес - ВТБ':
    deposit_sum(begin_sum, percent[7], period[7])
elif depos_name == '16% на 36мес - АльфаБанк':
    deposit_sum(begin_sum, percent[8], period[8])
else:
    deposit_sum(begin_sum, percent[9], period[9])
'''
deposit_sum(begin_sum, percent[depos_name], period[depos_name])