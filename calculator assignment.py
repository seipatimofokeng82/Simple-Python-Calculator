def calculator():
    while True:
        print("Simple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")

        choice = input("Choose an operation (1-5):")

        if choice not in ['1', '2', '3', '4', '5']:
            print("Error: Invalid choice. Please select a number between 1 and 5.")
            continue

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                result = num1 + num2
                operation = "Addition"
            elif choice == '2':
                result = num1 - num2
                operation = "Subtraction"
            elif choice == '3':
                result = num1 * num2
                operation = "Multiplication"
            elif choice == '4':
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                result = num1 / num2
                operation = "Division"
            else:
                raise ValueError("Invalid choice. Please select a number between 1 and 5.")

        except ValueError:
            print("Operation failed: ValueError! Non-numeric value entered.")
        except ZeroDivisionError as zde:
            print(f"Operation failed: {zde}")
        else:
            print(f"{operation} result: {result}")
            print("Operation successful.")

        finally:
            again = input("Do you want to perform another operation? (yes/no):").lower()
            if again != 'yes':
                print("Thank you for using the calculator!")
            
calculator()

















               


