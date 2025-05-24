while True:
    # Taking input from the user
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    operation = input("Please enter one of these operations (+, -, *, /, %, **): ")

    # List of operations that cannot have b as zero
    zero_error_operations = ["/", "%", "**"]

    # Checking if the operation is division, modulo, or exponentiation and if b is zero
    if operation in zero_error_operations and b == 0:
        print(f"Error: {operation} operation with zero is not allowed for 'b'.")
        b = int(input("Please enter a value for b other than 0: "))

    # Checking which operation to perform
    if operation == "+":
        sum_result = a + b
        print(f"The sum of {a} and {b} is: {sum_result}")

    elif operation == "-":
        subtraction = a - b
        print(f"The subtraction of {b} from {a} is: {subtraction}")

    elif operation == "*":
        multiplication = a * b
        print(f"The multiplication of {a} and {b} is: {multiplication}")

    elif operation == "/":
        division = a / b
        print(f"The division of {a} by {b} is: {division}")

    elif operation == "%":
        modulo = a % b
        print(f"The modulo of {a} by {b} is: {modulo}")

    elif operation == "**":
        exponentiation = a ** b
        print(f"The exponentiation of {a} to the power of {b} is: {exponentiation}")

    else:
        print("You are performing an invalid operation.")

    # Ask the user if they want to perform another operation
    another_operation = input("Do you want to perform another operation? (Yes/No): ").lower()

    if another_operation != "yes":
        print("Exiting the calculator. Thank you!")
        break
