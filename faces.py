# Define a function named 'convert' that takes an 'input_str' as a parameter
def convert(input_str):
    # Replace :) with 🙂
    input_str = input_str.replace(":)", "🙂")
    # Replace :( with 🙁
    input_str = input_str.replace(":(", "🙁")
    return input_str

# Explanation: The code defines a function named 'convert' that takes a string 'input_str' as a parameter. Inside this function, it replaces occurrences of ":)" with a smiling face emoji "🙂" and ":(" with a frowning face emoji "🙁". The modified string is then returned.

# Prompt the user for input
user_input = input("Type Hello :) and press Enter or Type Goodbye :( and press Enter: ")

# Explanation: The code uses the 'input()' function to prompt the user for input, displaying the message "Type Hello :) and press Enter or Type Goodbye :( and press Enter:".

# Call the convert function with user input
result = convert(user_input)

# Explanation: The 'convert' function is called with the user's input as an argument. This input string is passed to the 'convert' function, which replaces the smiley and frowning face emoticons with emojis as specified in the function.

# Display the converted text
print(result)

# Explanation: Finally, the code prints the converted text, which now contains emojis instead of the emoticons ":)" and ":(". This provides the user with the converted text, replacing emoticons with emojis.
