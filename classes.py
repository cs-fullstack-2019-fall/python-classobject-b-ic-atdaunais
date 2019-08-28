def main():
    myDinner = Dinner("Good dish", "Chicken", "Peas", "20.00")
    myDinner.printAttributes()
    kennAccount = Account("Kenn", "50", "08/28/2019")
    kevinAccount = Account("Kevin", "95", "08/28/2019")
    kennAccount.printNameAndBalance()
    kevinAccount.printNameAndBalance()
    kennAccount.updateBalance()
    kevinAccount.updateBalance()
    kennAccount.printNameAndBalance()
    kevinAccount.printNameAndBalance()


class Dinner:
    def __init__(self, dish, protein, veggie, price):
        self.dish = dish
        self.protein = protein
        self.veggie = veggie
        self.price = price

    def printAttributes(self):
        print(
            f"Dish name is: {self.dish}\nYour protein is: ${self.protein}\nThe veggie is: {self.veggie}\nYour total price is: ${self.price}")


class Account:
    def __init__(self, name, balance, creationDate):
        self.name = name
        self.balance = balance
        self.date = creationDate

    def updateBalance(self):
        userInput = input("Would you like to add (press 1) or remove (press 2) money from your account?\n")
        if userInput == "1":
            addMoney = int(input("How much would you like to add?\n"))
            self.balance = int(self.balance) + addMoney
            print(f"Your balance is now ${self.balance}")
        elif userInput == "2":
            subMoney = int(input("How much would you like to remove?\n"))
            self.balance = int(self.balance) - subMoney
            print(f"Your balance is now ${self.balance}")
        else:
            print("ERROR")

    def printNameAndBalance(self):
        print(f"Hello {self.name}! Your current balance is ${self.balance}")


main()
