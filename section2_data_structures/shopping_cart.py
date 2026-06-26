cart = []
categories = set()
item_prices = {}

def add_item():
    name = input("Enter item name: ").strip()
    category = input("Enter item category: ").strip()
    price = float(input("Enter item price: "))

    cart.append(name)
    categories.add(category)
    item_prices[name] = price
    print(f"'{name}' added to cart.")

def remove_item():
    name = input("Enter item name to remove: ").strip()
    if name in cart:
        cart.remove(name)
        del item_prices[name]
        print(f"'{name}' removed from cart.")
    else:
        print("Item not found in cart.")

def show_cart():
    if len(cart) == 0:
        print("Your cart is empty.")
        return

    print("\n" + "=" * 40)
    print("           YOUR CART")
    print("=" * 40)

    for item in cart:
        print(f"  {item}  :  Rs.{item_prices[item]:.2f}")

    print("-" * 40)
    print(f"  Categories    : {', '.join(categories)}")
    print(f"  Total Bill    : Rs.{sum(item_prices.values()):.2f}")
    print("=" * 40)

def main():
    print("=" * 40)
    print("       Shopping Cart System")
    print("=" * 40)

    while True:
        print("\n1. Add Item")
        print("2. Remove Item")
        print("3. View Cart and Total Bill")
        print("4. Exit")
        print("-" * 40)

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            show_cart()
        elif choice == "4":
            print("Thank you for shopping. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

main()