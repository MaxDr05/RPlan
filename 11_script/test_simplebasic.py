import pytest

# 假设有一个 BankAccount 类，包含以下方法：
#
# __init__(self, owner, balance=0): 初始化账户，设置所有者和初始余额
#
# deposit(self, amount): 存款方法，增加余额
#
# withdraw(self, amount): 取款方法，减少余额，如果余额不足则抛出 InsufficientFundsError 异常
#
# get_balance(self): 返回当前余额
#
# transfer(self, target_account, amount): 向目标账户转账

#自定义异常
class InsufficientFundsError(Exception):
    pass

#基础银行类
class BankAccount:
    def __init__(self, owner,balance=0):
        self._owner = owner
        if balance >= 0:
            self._balance = balance
        else:
            raise ValueError('Insufficient funds')

    @property
    def owner(self):
        return self._owner
    @owner.setter
    def owner(self,value):
        self._owner = value
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self,value):
        self._balance = value

    def deposit(self,amount):
        self._balance += amount

    def withdraw(self,amount):
        if amount > self._balance:
            raise InsufficientFundsError
        else:
            self._balance -= amount

    def transfer(self,target_account,amount):
        self.withdraw(amount)
        target_account.deposit(amount)

