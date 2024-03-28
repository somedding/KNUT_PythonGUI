from Account import *

accountsList = []

oAccount = Account('Joe', 100, 'JoesPassword')
accountsList.append(oAccount)
print("Joe's account number is 0")

oAccount = Account('Mary', 12345, 'MarysPassword')
accountsList.append(oAccount)
print("Mary's account number is 1")

oAccount = Account('Alex', 67890, 'AlexPassword')
accountsList.append(oAccount)
print("Alex's account number is 2")

accountsList[0].show()
accountsList[1].show()
accountsList[2].show()
print()

print('Calling methods of the two accounts ...')
accountsList[0].deposit(50, 'JoesPassword')
accountsList[1].withdraw(345, 'MarysPassword')
accountsList[1].deposit(100, 'MarysPassword')

accountsList[0].show()
accountsList[1].show()

print()
userName = input('What is the name for the new user account? ')
userBalance = input('What is the starting balance for this account? ')
userBalance = int(userBalance)
userPassword = input('What is the password you want to use for this account? ')
oAccount = Account(userName, userBalance, userPassword)
accountsList.append(oAccount)

print('Created new account, account number is 2')
accountsList[2].show()

accountsList[2].deposit(100, userPassword)
usersBalance = accountsList[2].getBalance(userPassword)
print()
print("After depositing 100, user's balance is:", usersBalance)

accountsList[2].show()
