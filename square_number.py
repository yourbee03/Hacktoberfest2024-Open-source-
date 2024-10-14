# Function to calculate the square of a number
def calculate_square(number):
    return number ** 2  # Using the exponentiation operator to calculate the square

# Example usage
num = float(input("Enter a number: "))  # Accepting a number from the user
square = calculate_square(num)  # Calculating the square
print(f"The square of {num} is {square}.")  # Displaying the result
