def calculator():
    print("\n--- Basic Calculator ---")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    while True:
        try:
            num2 = float(input("Enter second number: "))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    operation = input("Choose operation (+, -, *, /): ")

    if operation == "+":
        print("Result:", num1 + num2)
    elif operation == "-":
        print("Result:", num1 - num2)
    elif operation == "*":
        print("Result:", num1 * num2)
    elif operation == "/":
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Cannot divide by zero.")
    else:
        print("Invalid operation!")


def km_to_miles():
    while True:
        try:
            km = float(input("Enter kilometers: "))
            if km < 0:
                print("Distance cannot be negative.")
                continue
            print("Miles:", round(km * 0.621371, 2))
            break
        except ValueError:
            print("Invalid input! Enter a number.")


def celsius_to_fahrenheit():
    while True:
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9 / 5) + 32
            print("Fahrenheit:", round(fahrenheit, 2))
            break
        except ValueError:
            print("Invalid input! Enter a number.")


def main():
    while True:
        print("\n===== Interactive Calculator & Unit Converter =====")
        print("1. Basic Calculator")
        print("2. Kilometers to Miles")
        print("3. Celsius to Fahrenheit")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            calculator()
        elif choice == "2":
            km_to_miles()
        elif choice == "3":
            celsius_to_fahrenheit()
        elif choice == "4":
            print("Thank you for using the program!")
            break
        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()
