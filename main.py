wnted_priod = int(input('Введите количество месяцев, на котоорые вы хотите взять кредит: '))
wnted_percent = float(input('Введите желаемый процент: '))
begin_sum = float(input('Введите начальную сумму вклада: '))

percent = [11.5, 13.5, 14, 14.09, 14.75, 15, 15.25, 16, 16, 17]
period = [24, 12, 12, 6, 36, 3, 36, 6, 36, 12]

sum_of_priod = []


def deposit_sum(cash, percnt, time):
    for i in range(time):
        sum_of_priod.append(cash * (percnt / 100))
        cash += cash*(percnt/100)
    print('Сумма =', cash)
    print('Суммы в каждый месяц:', sum_of_priod)


if depos_name == '11.5% на 24мес - Тинькофф':
    deposit_sum(begin_sum, percent[0], period[0])
elif depos_name == '13.5% на 12мес - Тинькофф':
    deposit_sum(begin_sum, percent[1], period[1])
elif depos_name == '14% на 12мес - Сбер':
    deposit_sum(begin_sum, percent[2], period[2])
