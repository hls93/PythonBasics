from abc import ABCMeta, abstractmethod
from random import randint


class Account(metaclass = ABCMeta):
    @abstractmethod
    def createAccount():
        return 0

    @abstractmethod
    def authenticate():
        return 0

    @abstractmethod
    def withDrawl():
        return 0

    @abstractmethod
    def deposit():
        return 0

    @abstractmethod
    def displayBalance():
        return 0

class SavingsAccount(Account):
    def __init__(self):
        self.savingsAccounts = {}

    def createAccount(self, name, initialDeposit):
        self.accountNumber = randint(10000, 99999)
        self.savingsAccounts[self.accountNumber] = [name, initialDeposit]

    def authenticate(self, name, accountNumber):
        if accountNumber in self.savingsAccounts.keys():
            if self.savingsAccounts[accountNumber[0]] == name:
                print("Authentication Succesful")
                self.accountNumber = accountNumber
                return True
            else:
                print("Authentication failed")
                return False
        else:
            print("Authentication Failed")
            return False

    def withDrawl(self, withdrawelAmount):
        if withdrawelAmount > self.savingsAccounts[self.accountNumber][1]:
            print("Insufficient Balance")
        else:
            self.savingsAccounts[self.accountNumber][1] -= withdrawelAmount
            print("Withdrawal was successful. Available Balance: ", self.savingsAccounts[self.accountNumber[1]])


    def deposit(self, depositAmount):
        self.savingsAccounts[self.accountNumber][1] =+ depositAmount
        print("Deposit was successful. Available Balance: ", self.savingsAccounts[self.accountNumber[1]]")


    def displayBalance(self):
        print("Available Balance: ", self.savingsAccounts[self.accountNumber][1])