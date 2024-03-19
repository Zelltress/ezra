import ru_local as ru

wnted_priod = int(input(ru.CHOICE_PRD))
wnted_percent = float(input(ru.CHOICE_PRCNT))
begin_sum = float(input(ru.CHOICE_DPST))


sum_of_priod = []
NashP = []
Nash = []
new = []

percent = [15, 13.5, 11.5, 14, 16, 14.09, 13.8, 16, 12.5, 11.5]
period = [3, 12, 24, 12, 6, 12, 24, 36, 12, 36]


def check_exists_period(wnted_priod):
    return wnted_priod != 0 and wnted_priod >= 1


def check_exists_percent(wnted_percent):
    return wnted_percent != 0


for i in range(0, 10):
    if period[i] == wnted_priod:
        NashP.append(i)
        print(i, NashP)

for k in NashP:
    print(percent[k])
    Nash.append(percent[k])

for f in range(0, len(Nash)):
    if Nash[f] == wnted_percent:
        depos_name = f + 1



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


def deposit_sum(cash, percnt, time):
    for i in range(time):
        sum_of_priod.append(cash * (percnt / 100))
        cash += cash * (percnt / 100)
    print(ru.CASH, cash)
    print(ru.SUMM_OF_PRD, sum_of_priod)



