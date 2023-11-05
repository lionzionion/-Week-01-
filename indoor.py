# Pass a custom string as an argument to input
user_input = input("Welcome to my first Python program, what's your name?: ")

# Explanation: The code above uses the input() function to prompt the user for their name. The text "Welcome to my first Python program, what's your name?:" is displayed as a prompt, allowing the user to enter their name as a response.

# Convert the input to lowercase
lowercase_input = user_input.lower()

# Explanation: After the user enters their name, the code converts the input to lowercase using the lower() method. This is done to ensure that the name is in lowercase format, making it easier to handle and compare in the future.

# Output the lowercase input along with "You're welcome"
print("You're welcome,")
print(lowercase_input)

# Explanation: Finally, the code prints a friendly message "You're welcome," followed by the user's name in lowercase. This provides a polite response to the user and displays their name in the same case as the rest of the message. The use of the lowercase name ensures consistency in the output.
