




## FUNCTION - CALCULATOR

class Calculator:
    def perform_operation(self, operation, num1, num2=None):
        num1 = float(num1)
        if num2 is not None:
            num2 = float(num2)
        
        if operation == 'add':
            return num1 + num2
        elif operation == 'subtract':
            return num1 - num2
        elif operation == 'multiply':
            return num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                raise ValueError("Cannot divide by zero")
            return num1 / num2
        elif operation == 'square':
            return num1 ** 2
        elif operation == 'sqrt':
            if num1 < 0:
                raise ValueError("Cannot calculate square root of negative number")
            return num1 ** 0.5
        else:
            raise ValueError("Invalid operation")