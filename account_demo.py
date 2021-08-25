'''
Эта программа создаёт экземпляр класса
SavinsAccount и экземпляр класса CD.
'''

import accounts
from depoCD import CD

seps = '-' * 35

def main():
    # Получить номер счёта, процентную ставку,
    # остаток сберегательного счёта.

    print('Введите данные о сберегательном счёте.')
    print(seps)
    acct_num = input('Номер счёта: ')
    int_rate = float(input('Процентная ставка: '))
    balance = float(input('Остаток: '))

    # Создаём объект SavingsAccount.
    savings = accounts.SavingsAccount(acct_num, int_rate, balance)

    # Получить номер счёта, процентную ставку,
    # остаток счёта и дату погашения счёта CD.
    print('Введите данные о счёте CD: ')
    acct_num = input('Номер счёта: ')
    int_rate = float(input('Процентная ставка: '))
    balance = float(input('Остаток: '))
    mat_date = input('Дата погашения: ')

    # Создаём объект CD.
    cd = CD(acct_num, int_rate, balance, mat_date)

    # Показать введённые данные.
    print(seps)
    print('Вот введённые Вами данные: ')
    print()
    print('Сберегательный счёт.')
    print()
    print('Номер счёта: ', savings.get_account_num())
    print('Процентная ставка: ', savings.get_int_rate())
    print('Остаток: ', format(savings.get_balance(), '.2f'), sep='')
    print()
    print(seps)
    print('Счёт депозитного сертификата CD: ')
    print()
    print('Номер счёта: ', cd.get_account_num())
    print('Процентная ставка: ', cd.get_int_rate())
    print('Остаток: ', format(cd.get_balance(), '.2f'), sep='')
    print('Дата погашения: ', cd.get_maturity_date())
    print(seps)


main()
