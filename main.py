import ru_local as ru

wnted_prd = int(input(ru.CHOICE_PRD))
wnted_prcnt = float(input(ru.CHOICE_PRCNT))
begin_sum = float(input(ru.CHOICE_DPST))

sum_of_prd = []
nashP = []
nash = []
new = []

percent = [15, 13.5, 11.5, 14, 16, 14.09, 13.8, 16, 12.5, 11.5]
period = [3, 12, 24, 12, 6, 12, 24, 36, 12, 36]


def check_exists(wnted_prd, wnted_prcnt, begin_sum):
    '''
    This function checks whether it is possible to make a deposit according to the entered conditions
    '''
    return wnted_prd != 0 and wnted_prd >= 1 and wnted_prcnt != 0 and begin_sum != 0


def suitable_dpst(wnted_prd, wnted_prcnt):
    '''
    This function finds the most suitable contribution based on the entered values
    '''
    global depos_name
    for i in range(0, 10):
        if period[i] == wnted_prd:
            nashP.append(i)
            print(i, nashP)

    for k in nashP:
        print(percent[k])
        nash.append(percent[k])

    for f in range(0, len(nash)):
        if nash[f] == wnted_prcnt:
            depos_name = f + 1

    return depos_name


def deposits_descr(depos_name):
    '''
    In this function we display a description of the deposits
    '''
    match depos_name:
        case 0:
            print(ru.TINKOFF_3)
        case 1:
            print(ru.TINKOFF_12)
        case 2:
            print(ru.TINKOFF_24)
        case 3:
            print(ru.SBERBANK_12)
        case 4:
            print(ru.VTB_6)
        case 5:
            print(ru.VTB_12)
        case 6:
            print(ru.ALFABANK_24)
        case 7:
            print(ru.ALFABANK_36)
        case 8:
            print(ru.LEVOBEREZHNY_12)
        case 9:
            print(ru.LEVOBEREZHNY_36)


def deposit_sum(cash, prcnt, time):
    '''
    This function calculates the deposit amount at the end of the term and accruals for each month
    '''
    for i in range(time):
        sum_of_prd.append(cash * (prcnt / 100))
        cash += cash * (prcnt / 100)
    print(ru.CASH, cash)
    print(ru.SUMM_OF_PRD, sum_of_prd)


def main():
    if check_exists(wnted_prd, wnted_prcnt, begin_sum):
        suitable_dpst()
        deposits_descr()
        deposit_sum()
    else:
        print(ru.DISPARITY)



if __name__ == '__main__':
    main()
