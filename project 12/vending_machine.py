# Vending Machine

items = {
    1: ["Chips", 20, 5],
    2: ["Chocolate", 30, 4],
    3: ["Biscuits", 15, 6],
    4: ["Juice", 25, 3]
}


def display_items():
    print("\n========== VENDING MACHINE ==========")
    for number, item in items.items():
        print(number, ".", item[0], "- Rs.", item[1], "| Stock:", item[2])
    print("======================================")


def purchase_item(choice, money):
    if choice not in items:
        return "Invalid choice"

    name, price, stock = items[choice]

    if stock <= 0:
        return "Item out of stock"

    if money < price:
        return "Insufficient money"

    items[choice][2] -= 1
    change = money - price

    return "Dispensing " + name + ". Change: Rs." + str(change)


def vending_machine():
    while True:
        display_items()

        try:
            choice = int(input("Enter item number (0 to exit): "))

            if choice == 0:
                print("Thank you for using the vending machine!")
                break

            if choice not in items:
                print("Invalid choice!")
                continue

            money = int(input("Enter money: Rs. "))

            result = purchase_item(choice, money)
            print(result)

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    vending_machine()