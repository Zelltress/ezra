import ru_local as ru
import math

wnted_prd = int(input(ru.CHOICE_PRD))
wnted_prcnt = float(input(ru.CHOICE_PRCNT))
begin_sum = float(input(ru.CHOICE_DPST))

sum_of_prd = []
required_prd = []
required_prcnt = []
new = []
final = []
variant = []


percent = [15, 13.5, 11.5, 14, 16, 14.09, 13.8, 16, 12.5, 11.5]
period = [3, 12, 24, 12, 6, 12, 24, 36, 12, 36]


def check_exists():
    '''
    This function checks whether it is possible to make a deposit according to the entered conditions
    '''
    return wnted_prcnt > 0 and begin_sum > 0 and wnted_prd in period


def suitable_dpst():
    '''
    This function finds the most suitable contribution based on the entered values
    '''
    for i in range(0, 10):
        if period[i] == wnted_prd:
            required_prd.append(i)

    for k in required_prd:
        required_prcnt.append(percent[k])

    for f in range(0, len(required_prcnt)):
        if required_prcnt[f] == wnted_prcnt:
            variant.append(required_prd[f])
            final.append(f)

    if len(final) == 0:
        for a in required_prcnt:
            a = a - wnted_prcnt
            new.append(math.fabs(a))
        for number in range(0, len(required_prcnt)):
            if new[number] == min(new):
                variant.append(required_prd[number])

    
def deposits_descr():
    '''
    In this function we display a description of the deposits
    '''
    print(ru.ANSWER)
    for depos_name in variant:
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
    if check_exists():
        suitable_dpst()
        deposits_descr()
        for depos_name in variant:
            deposit_sum(begin_sum, percent[depos_name], period[depos_name])
    else:
        print(ru.DISPARITY)


if __name__ == '__main__':
    main()
