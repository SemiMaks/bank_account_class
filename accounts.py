'''
Класс SavingAccount представляет
сберегательный счёт.
'''


class SavingsAccount:
    # Метод __init__ принимает аргументы для
    # номера счёта, процентной ставки и остатка

    def __init__(self, account_num, int_rate, bal):
        self.__account_mum = account_num
        self.__interest_rate = int_rate
        self.__balance = bal

    # Следующие ниже методы являются методами-
    # модификаторами атрибутов данных.

    def set_account_num(self, account_num):
        self.__account_mum = account_num

    def set_interest_rate(self, int_rate):
        self.__interest_rate = int_rate

    def set_balance(self, bal):
        self.__balance = bal

    # Методы-получатели атрибутов данных

    def get_account_num(self):
        return self.__account_mum

    def get_int_rate(self):
        return self.__interest_rate

    def get_balance(self):
        return self.__balance
