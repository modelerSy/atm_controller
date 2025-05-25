
from atm import Account, BankSystem, ATMController

def test_atm_flow():
    bank = BankSystem()
    acc = Account("12345", "4321", balance=100)
    bank.add_account(acc)

    atm = ATMController(bank)

    assert atm.insert_card("12345") == True

    assert atm.enter_pin("0000") == False

    atm.insert_card("12345")
    assert atm.enter_pin("4321") == True

    assert atm.check_balance() == 100

    atm.deposit(50)
    assert atm.check_balance() == 150

    atm.withdraw(30)
    assert atm.check_balance() == 120

    print("tests passed!")

if __name__ == "__main__":
    test_atm_flow()
