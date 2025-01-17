def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 != 0:
            return num1/num2
        else:
            print('Error. Division by zero is not allowed!')
    else:
        print('Error. You used an incorrect operation.')

if __name__ == "__main__": 
    num1 = 5.0 
    num2 = 0.0 
    operation = "divide" 
    result = perform_operation(num1, num2, operation) 
    print(f"Result: {result}")