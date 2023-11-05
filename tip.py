# Define a function named 'main'
def main():
    # Prompt the user for the cost of the meal and the desired tip percentage
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    
    # Check if valid input was provided
    if dollars is not None and percent is not None:
        # Calculate the tip amount
        tip = dollars * percent
        # Print the tip amount with two decimal places
        print(f"Leave ${tip:.2f}")

# Define a function named 'dollars_to_float' to convert a dollar amount to a float
def dollars_to_float(x):
    try:
        # Remove the dollar sign and convert the input to a float
        x = x.replace('$', '')
        return float(x)
    except ValueError:
        # Handle invalid input and provide an error message
        print("Invalid input. Please enter a valid dollar amount.")
        return None

# Define a function named 'percent_to_float' to convert a percentage to a float
def percent_to_float(y):
    try:
        # Remove the percentage sign (%) and convert the input to a float
        y = y.replace('%', '')
        percent = float(y)
        if percent >= 0 and percent <= 100:
            # Convert the percentage to a decimal between 0 and 1
            return percent / 100.0
        else:
            # Handle out-of-range input and provide an error message
            print("Invalid input. Please enter a valid percentage between 0 and 100.")
            return None
    except ValueError:
        # Handle invalid input and provide an error message
        print("Invalid input. Please enter a valid percentage between 0 and 100.")
        return None

# Call the 'main' function to execute the program
main()
