import ru_local as ru
wnted_priod = int(input('Введите количество месяцев, на котоорые вы хотите взять вклад: '))
wnted_percent = float(input('Введите желаемый процент: '))
begin_sum = float(input('Введите начальную сумму вклада: '))

percent = [15, 13.5, 11.5, 14, 16, 14.09, 13.8, 16, 12.5, 11.5]
period = [3, 12, 24, 12, 6, 12, 24, 36, 12, 36]

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
    case 0:
        description = ru.TINKOFF_3
        print(ru.TINKOFF_3)
    case 1:
        description = ru.TINKOFF_12
        print(ru.TINKOFF_12)
    case 2:
        description = ru.TINKOFF_24
        print(ru.TINKOFF_24)
    case 3:
        description = ru.SBERBANK_12
        print(ru.SBERBANK_12)
    case 4:
        description = ru.VTB_6
        print(ru.VTB_6)
    case 5:
        description = ru.VTB_12
        print(ru.VTB_12)
    case 6:
        description = ru.ALFABANK_24
        print(ru.ALFABANK_24)
    case 7:
        description = ru.ALFABANK_36
        print(ru.ALFABANK_36)
    case 8:
        description = ru.LEVOBEREZHNY_12
        print(ru.LEVOBEREZHNY_12)
    case 9:
        description = ru.LEVOBEREZHNY_36
        print(ru.LEVOBEREZHNY_36)


def check_exists_period(wnted_priod):
    return wnted_priod != 0 and wnted_priod >= 1

def check_exists_percent(wnted_percent):
    return wnted_percent != 0



# Можно попробовать такой вариант, чтобы там были True, False
values = []
def option_existence():
    for i in range(len(percent)):
        values.append(period[i] == wnted_priod and percent[i] == wnted_percent)
    return sum(values)


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