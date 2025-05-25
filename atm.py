# Insert Card => PIN number => Select Account => See Balance/Deposit/Withdraw 


class Account:
    def __init__(self, account_id, pin, balance=0):
        self.account_id = account_id
        self._pin = pin  # 외부에서는 pin 값에 직접 접근 불가
        self.balance = balance

    def verify_pin(self, pin):
        return self._pin == pin

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self):
        return self.balance


class BankSystem:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_id] = account

    def authenticate(self, account_id, pin):
        account = self.accounts.get(account_id)
        return account and account.verify_pin(pin)

    def get_account(self, account_id):
        return self.accounts.get(account_id)


class ATMController:
    def __init__(self, bank_system):
        self.bank = bank_system
        self.current_account = None

    def insert_card(self, account_id):
        self.current_account = self.bank.get_account(account_id)
        return self.current_account is not None

    def enter_pin(self, pin):
        if self.current_account and self.current_account.verify_pin(pin):
            return True
        self.current_account = None
        return False

    def check_balance(self):
        return self.current_account.get_balance()

    def deposit(self, amount):
        self.current_account.deposit(amount)

    def withdraw(self, amount):
        self.current_account.withdraw(amount)
