from bank_account import BankAccount

class CheckingAccount(BankAccount):
    transferLimit = 6

    def __init__(self, customer_name, current_balance, minimum_balance:float, transfer_limit: int = transferLimit):
        super().__init__(customer_name, current_balance, minimum_balance)
        self.__transfer_limit = transfer_limit
        self.__transfers_used = 0

    def withdraw(self, withdraw_amount:float):
        if self.__transfers_used >= self.__transfer_limit:
            print("Cannot withdraw, monthly transfer limit reached")
            return
        before = self.current_balance
        super().withdraw(withdraw_amount)
        if self.current_balance < before:
            self.__transfers_used += 1
            remaining = self.__transfer_limit - self.__transfers_used
            print(f"Remaining transfers: {remaining}")

    def transfer(self, target_account: BankAccount, transfer_amount:float):
        before = self.current_balance
        self.withdraw(transfer_amount)
        if self.current_balance < before:
            target_account.deposit(transfer_amount)

    def print_customer_information(self):
        super().print_customer_information()
        print(f"Transfer limit: {self.__transfer_limit}")
        print(f"Transfer used: {self.__transfers_used}")
        print("Account Type: Checking")