from bank_account import BankAccount

class SavingsAccount(BankAccount):
    interestRate = 0.05

    def __init__(self, customer_name:str, current_balance:float, minimum_balance:float, interest_rate:float=interestRate):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.interest_rate = interest_rate

    def interest(self):
        interest = round(self.current_balance * (self.interest_rate / 12), 2)
        self.current_balance += interest
        print(f"Interest of ${interest:.2f} applied. New Balance: ${self.current_balance:.2f}")

    def print_customer_information(self):
        super().print_customer_information()
        print(f"Annual rate: {self.interest_rate * 100:.2f}%")
        print(f"Account Type: Savings Account")