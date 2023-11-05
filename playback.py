# Prompt the user for input
user_input = input("Type a sentence: ")

# Explanation: In this part of the code, the user is prompted to input a sentence. The `input()` function displays the message "Type a sentence:" and waits for the user to provide their input.

# Replace spaces with three periods and print the result
output = user_input.replace(' ', '...')

# Explanation: After the user enters their sentence, the code uses the `replace()` method to replace all spaces (' ') with three periods ('...'). This means that every space in the sentence will be replaced by three periods. The result is stored in the variable 'output'.

# Print the modified sentence
print(output)

# Explanation: Finally, the modified sentence, where spaces have been replaced with three periods, is printed to the console. This part of the code displays the transformed sentence to the user.
