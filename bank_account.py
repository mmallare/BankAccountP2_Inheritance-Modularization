import random
class BankAccount:
    bank_title = "Class Bank"
    def __init__(self, customer_name:str, current_balance:float, minimum_balance:float):
        self.customer_name = customer_name
        self.current_balance = current_balance
        self.minimum_balance = minimum_balance

        self._account_number = str(random.randint(1_000_000_000, 9_999_999_999))
        self.__routing_number = "021000021"

    def get_account_number(self):
        return "******" + self._account_number

    def get_routing_number(self):
        return self.__routing_number

    def deposit(self, deposit_amount:float):
        if deposit_amount <= 0:
            print("You cannot deposit negative amounts")
            return
        self.current_balance += deposit_amount
        print("Deposited")

    def withdraw(self, withdraw_amount:float):
        if withdraw_amount <= 0:
            print("Cannot withdraw negative amount")
            return
        if self.current_balance - withdraw_amount < self.minimum_balance:
            print("Cannot withdraw, minimum balance reached")
            return
        self.current_balance -= withdraw_amount
        print("Withdrew")

    def print_customer_information(self):
        print("Bank:", BankAccount.bank_title)
        print("Customer Name:", self.customer_name)
        print("Current Balance:", self.current_balance)
        print("Minimum Balance:", self.minimum_balance)