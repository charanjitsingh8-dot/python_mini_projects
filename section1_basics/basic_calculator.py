def get_number(prompt):
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")


def calculator():
    print("=" * 40)
    print("       Welcome to Basic Calculator")
    print("=" * 40)

    while True:
        print("\nOperations: + | - | * | /")
        print("-" * 40)

        num1 = get_number("Enter first number: ")

        operator = input("Enter operator (+, -, *, /): ").strip()

        if operator not in ["+", "-", "*", "/"]:
            print("Invalid operator! Please use +, -, *, /\n")
            continue

        num2 = get_number("Enter second number: ")

        if operator == "+":
            result = num1 + num2
            print(f"\nDone! {num1} + {num2} = {result}")
        elif operator == "-":
            result = num1 - num2
            print(f"\nDone! {num1} - {num2} = {result}")
        elif operator == "*":
            result = num1 * num2
            print(f"\nDone! {num1} x {num2} = {result}")
        elif operator == "/":
            if num2 == 0:
                print("\nError: Division by zero is not allowed!")
            else:
                result = num1 / num2
                print(f"\nDone! {num1} / {num2} = {result:.4f}")

        print("-" * 40)
        again = input("Calculate again? (yes/no): ").strip().lower()
        if again != "yes":
            print("\nThanks for using the calculator. Goodbye!")
            print("=" * 40)
            break


calculator()