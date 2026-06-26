def log_expense():
    try:
        category = input("Enter category (e.g. Food, Travel, Shopping): ").strip()
        description = input("Enter description: ").strip()
        amount = float(input("Enter amount spent: Rs."))

        with open("expenses.txt", "a") as file:
            file.write(f"{category},{description},{amount}\n")

        print("Expense logged successfully.")

    except ValueError:
        print("Invalid amount. Please enter a valid number.")


def show_summary():
    try:
        summary = {}

        with open("expenses.txt", "r") as file:
            lines = file.readlines()

        if not lines:
            print("No expenses recorded yet.")
            return

        for line in lines:
            parts = line.strip().split(",")
            if len(parts) == 3:
                category = parts[0]
                amount = float(parts[2])
                if category in summary:
                    summary[category] += amount
                else:
                    summary[category] = amount

        print("\n" + "=" * 40)
        print("        EXPENSE SUMMARY")
        print("=" * 40)
        for category, total in summary.items():
            print(f"  {category}  :  Rs.{total:.2f}")
        print("-" * 40)
        print(f"  Total Spent  :  Rs.{sum(summary.values()):.2f}")
        print("=" * 40)

    except FileNotFoundError:
        print("No expense file found. Please log an expense first.")


def main():
    print("=" * 40)
    print("          Expense Tracker")
    print("=" * 40)

    while True:
        print("\n1. Log Expense")
        print("2. View Summary by Category")
        print("3. Exit")
        print("-" * 40)

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "1":
            log_expense()
        elif choice == "2":
            show_summary()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

main()