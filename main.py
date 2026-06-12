from savings_account import SavingsAccount
from checkings_account import CheckingAccount

ashlin = CheckingAccount("Ashlin", 1000, 100)
ashlin.print_customer_information()
ashlin.withdraw(200)
ashlin.withdraw(100)
ashlin.withdraw(50)

mike = SavingsAccount("Mike", 500, 50)
ashlin.transfer(mike, 100)

mike.interest()
mike.print_customer_information()
print()
customer1 = CheckingAccount("Name1", 500, 200)
customer1.print_customer_information()
customer2 = CheckingAccount("Name2", 2000, 200)
customer2.print_customer_information()

customer3 = SavingsAccount("Name3", 800, 150)
customer3.print_customer_information()
customer4 = SavingsAccount("Name4", 2500, 300)
customer4.print_customer_information()