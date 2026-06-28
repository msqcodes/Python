print("--------------------")
print("      MSQ ATM")
print("--------------------")

system_pin = 9705
user_pin = int(input("Enter your PIN : "))

if user_pin != system_pin:
    print("Invalid PIN")
else:
    balance = int(input("Enter Initial Balance : "))

    while True:

        print("\n--------------------")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print("--------------------")

        option = int(input("Choose Option : "))

        if option == 1:

            print("--------------------")
            print(f"Current Balance : ₹{balance}")
            print("--------------------")

        elif option == 2:

            deposit = int(input("Deposit Amount : "))

            if deposit <= 0:
                print("Invalid Deposit Amount")
            else:
                balance += deposit
                print("--------------------")
                print("Successfully Deposited")
                print(f"Current Balance : ₹{balance}")
                print("--------------------")

        elif option == 3:

            withdraw = int(input("Withdraw Amount : "))

            if withdraw <= 0:
                print("Invalid Withdrawal Amount")

            elif withdraw > balance:
                print("--------------------")
                print("Insufficient Balance")
                print(f"Current Balance : ₹{balance}")
                print("--------------------")

            else:
                balance -= withdraw
                print("--------------------")
                print("Successfully Withdrawn")
                print(f"Current Balance : ₹{balance}")
                print("--------------------")

        elif option == 4:

            print("--------------------")
            print("Thank You! Visit Again")
            print("--------------------")
            break

        else:
            print("Invalid Option")
