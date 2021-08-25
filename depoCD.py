'''
Класс CD представляет счёт
депозитного сертификата (CD).
Это подкласс класса SavingAccount.
'''

from accounts import SavingsAccount


class CD(SavingsAccount):
    # Метод __init__ принимает аргументы для
    # номера счёта, процентной ставки, остатка
    # и даты погашения.

    def __init__(self, account_num, int_rate, bal, mat_date):
        # Вызов метода __init__ надкласса.
        SavingsAccount.__init__(self, account_num, int_rate, bal)

        # Инициализируем атрибут __maturity_date.
        self.__maturity_date = mat_date

    # Метод set_maturity модификатор атрибута __maturity_date.
    def set_maturity_date(self, mat_date):
        self.__maturity_date = mat_date

    # Метод get_maturity получатель атрибута __maturity_date.
    def get_maturity_date(self):
        return self.__maturity_date
