CORRECT_PIN = "1234"
balance = 10000.0
max_attempts = 3
attempts = 0

print("=" * 40)
print("        Welcome to Python ATM")
print("=" * 40)

while attempts < max_attempts:
    pin = input("Please enter your PIN: ")
    if pin == CORRECT_PIN:
        print("\nPIN Correct! Access Granted.\n")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Wrong PIN! {remaining} attempt(s) remaining.\n")
        else:
            print("Card blocked! Too many wrong attempts. Goodbye.")
            exit()

while True:
    print("-" * 40)
    print("         ATM MENU")
    print("-" * 40)
    print("  1. Check Balance")
    print("  2. Deposit Money")
    print("  3. Withdraw Money")
    print("  4. Exit")
    print("-" * 40)
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        print(f"\nYour current balance is: Rs.{balance:.2f}\n")

    elif choice == "2":
        amount_input = input("Enter amount to deposit: Rs.")
        if not amount_input.isdigit():
            print("Invalid amount! Please enter a number.\n")
        else:
            amount = float(amount_input)
            if amount <= 0:
                print("Amount must be greater than zero!\n")
            else:
                balance += amount
                print(f"Rs.{amount:.2f} deposited successfully!")
                print(f"New Balance: Rs.{balance:.2f}\n")

    elif choice == "3":
        amount_input = input("Enter amount to withdraw: Rs.")
        if not amount_input.isdigit():
            print("Invalid amount! Please enter a number.\n")
        else:
            amount = float(amount_input)
            if amount <= 0:
                print("Amount must be greater than zero!\n")
            elif amount > balance:
                print(f"Insufficient balance! Your balance is Rs.{balance:.2f}\n")
            else:
                balance -= amount
                print(f"Rs.{amount:.2f} withdrawn successfully!")
                print(f"Remaining Balance: Rs.{balance:.2f}\n")

    elif choice == "4":
        print("\nThank you for using Python ATM. Goodbye!")
        print("=" * 40)
        break

    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.\n")