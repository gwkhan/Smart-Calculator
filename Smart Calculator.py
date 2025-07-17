# Smart Calculator CLI Project (Bill + Arithmetic)

total = 0

def bill_calculator():
    global total
    total = 0
    while True:
        value = input("Enter product value or type 'enough' to finish: ")
        if value.lower() == "enough":
            break
        try:
            price = float(value)
            total += price
        except ValueError:
            print("❌ Please enter a valid number.")

    try:
        discount = float(input("Enter discount percentage: "))
        discounted = discount / 100 * total
        final = round(total - discounted, 2)
        print(f"✅ Your total bill after {discount}% discount is: ₹{final}")
    except ValueError:
        print("❌ Invalid discount. No discount applied.")
        print(f"✅ Your total bill: ₹{round(total, 2)}")

def arithmetic_calculator():
    while True:
        expression = input("Enter operation (e.g., 5 + 3) or type 'exit' to stop: ")
        if expression.lower() == "exit":
            break
        parts = expression.split()
        if len(parts) != 3:
            print("❌ Invalid format. Use format like: 5 + 2")
            continue
        num1, operator, num2 = parts
        try:
            c = float(num1)
            d = float(num2)
        except ValueError:
            print("❌ Invalid numbers.")
            continue

        if operator == '+':
            print(f"✅ {c} + {d} = {c + d}")
        elif operator == '-':
            print(f"✅ {c} - {d} = {c - d}")
        elif operator == '*':
            print(f"✅ {c} * {d} = {c * d}")
        elif operator == '/':
            if d == 0:
                print("❌ Cannot divide by zero.")
            else:
                print(f"✅ {c} / {d} = {c / d}")
        else:
            print("❌ Invalid operator. Use +, -, *, or /.")

def main():
    while True:
        print("\n--- Smart Calculator ---")
        print("1. Total Bill Calculator")
        print("2. Arithmetic Calculator")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            bill_calculator()
        elif choice == "2":
            arithmetic_calculator()
        elif choice == "3":
            print("Thank you for using Smart Calculator!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()