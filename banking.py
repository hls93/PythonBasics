from abc import ABCMeta, abstractmethod
from random import randint


class Account(metaclass = ABCMeta):
    @abstractmethod
    def createAccount(self):
        return 0

    @abstractmethod
    def authenticate(self):
        return 0

    @abstractmethod
    def withDrawl(self):
        return 0

    @abstractmethod
    def deposit(self):
        return 0

    @abstractmethod
    def displayBalance(self):
        return 0

class SavingsAccount(Account):
    def __init__(self):
        self.savingsAccounts = {}

    def createAccount(self, name, initialDeposit):
        self.accountNumber = randint(10000, 99999)
        self.savingsAccounts[self.accountNumber] = [name, initialDeposit]
        print("You account number is: ", self.accountNumber)

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
            print("Withdrawal was successful.")
            self.displayBalance()

    def deposit(self, depositAmount):
        self.savingsAccounts[self.accountNumber][1] =+ depositAmount
        print("Deposit was successful.")
        self.displayBalance()

    def displayBalance(self):
        print("Available Balance: ", self.savingsAccounts[self.accountNumber][1])

savingsAccount = SavingsAccount()
while True:
    print("Enter 1 to create a new account")
    print("Enter 2 to access and existing account")
    print("Enter 3 to exit")
    userChoice = int(input())
    if userChoice is 1:
        print("Enter your name: ")
        name = input()
        print("Enter the intial deposit: ")
        deposit = int(input())
        savingsAccount.createAccount(name, deposit)
    elif userChoice is 2:
        print("Enter your name: ")
        name = input()
        print("Enter your account number: ")
        accountNumber = int(input)
        authStatus = savingsAccount.authenticate(name, accountNumber)
        if authStatus is True:
            while True:
                print("Enter 1 to withdraw, 2 to deposit, or 3 to display available balance. Or enter 4 to go back the previous menu")
                userChoice = int(input())
                if userChoice is 1:
                    print("Enter a withdrawal amount")
                    withdrawalAmount = int(input())
                    savingsAccount.withDrawl(withdrawalAmount)
                elif userChoice is 2:
                    print("Enter a deposit amount")
                    depositAmount = int(input())
                    savingsAccount.deposit(depositAmount)
                elif userChoice is 3:
                    savingsAccount.displayBalance()
                elif userChoice is 4:
                    break
    elif userChoice is 3:
            quit()