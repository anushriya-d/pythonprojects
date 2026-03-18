# Banking Program

def balance(current_balance):
    print("------------------------------------")
    print(f"Your current balance is ₹{current_balance:.2f}")
    print("------------------------------------")

def deposit():
    print("------------------------------------")
    amount = float(input("Enter your amount to be deposited -> "))
    print("------------------------------------")

    if amount<0:
        print("------------------------------------")
        print("Please enter a valid amount.")
        print("------------------------------------")
        return 0
    else:
        return amount

def withdraw(current_balance):
    print("------------------------------------")
    amount= float(input("enter the aunt you want to withdraw -> "))
    print("------------------------------------")    

    if amount > current_balance:
        print("------------------------------------")
        print("Given amount is invalid.")
        print("------------------------------------")
        return 0
    elif amount < 0:
        print("------------------------------------")
        print("The amount should be more than 0.")
        print("------------------------------------")
        return 0
    else:
        return amount


def main():
    current_balance = 0
    running = True

    while running:
        print("------------------------------------")
        print("       # Banking Program #          ")
        print("1.Balance")
        print("2.Deposits")
        print("3.Withdrawl")
        print("4.Exit")
        print("------------------------------------")

        choice = input("Enter your choice (1-4): ")
        print("------------------------------------")

        if choice == '1':
            balance(current_balance)
        elif choice == '2':
            current_balance += deposit()
        elif choice == '3':
            current_balance -= withdraw(current_balance)
        elif choice == '4':
            running = False
        else:
            print("------------------------------------")
            print("Enter the valid choice.")
            print("------------------------------------")

    print("Thank you! HAVE A NICE DAY")

if __name__ == '__main__':
    main()