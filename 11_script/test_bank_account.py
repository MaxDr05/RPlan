# 1\测试账户初始化
# 测试新账户的余额是否正确
# 测试账户所有者名称是否正确
# 2\测试存款功能
# 测试正常存款
# 测试存款负数的异常情况（应该抛出 ValueError）
# 3\测试取款功能
# 测试正常取款
# 测试取款金额超过余额的情况（应该抛出 InsufficientFundsError）
# 测试取款负数的异常情况

import pytest
from test_simplebasic import BankAccount

@pytest.fixture(scope='function',autouse=True)
def bank_fixture():
    print('test_start------------------')
    yield
    print('test_end-------------------')

class Test_bankAccount_init():

    def test_create(self):
        Calvin_Account = BankAccount("Calvin", 100)
        assert Calvin_Account.balance == 100
        assert Calvin_Account.owner == 'Calvin'


    def test_create2(self):
        ZeroAccount = BankAccount("Zero")
        assert ZeroAccount.balance == 0
        assert ZeroAccount.owner == 'Zero'

    def test_create3(self):
        with pytest.raises(ValueError,match='Insufficient funds'):
            minusAccount = BankAccount("Minus",balance=-100)




