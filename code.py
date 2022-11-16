class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin
    
    def check_balance(self):
        print("Your balance is : 50000")

    def withdrawl(self, amount):
        new_amount = 50000 - amount
        print("You have withdrawn amount : " + str(amount) + ". Your remaining balance is : " + str(new_amount))

def main():
    card_number = input("Insert your cardnumber : ")
    pin_number = input("Enter your pin number : ")
    new_user = Atm(card_number, pin_number)
    print("Choose your activities")
    print("1. Balance Enquiry  2. Withdrawl")
    activity = int(input("Enter activity number : "))
    if(activity == 1):
        new_user.check_balance()
    elif(activity == 2):
        amount = int(input("Enter the amount : "))
        new_user.withdrawl(amount)
    else:
        print("Enter a valid number")

if __name__ == "__main__":
    main()

