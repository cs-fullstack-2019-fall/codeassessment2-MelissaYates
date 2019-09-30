# ### Problem 4
# Write a program that allows users to compare words by their length.
# Implement a function called chk_strings that accepts 2 strings entered by the user and compares them by length
# The function should return true if the first string parameter has more characters (i.e. longer)
# than the second string passed into the function, otherwise, the function should return false.
# DO NOT print the result in the function, print the result using the return value provided by the function. 

# Example Input/Output:
# ```
# Enter the first string: BIRD
# Enter the second string: COW

# BIRD is longer than COW
# ```

def chk_strings(user_string1, user_string2):
    if user_string1 > user_string2:
        return True
    elif user_string1 < user_string2:
        return False


user_input = input("Enter a word")
user_input2 =input("Enter a second word")

chk_strings()