# ### Problem 1
# Ask the user to enter a number. 
# Using the provided list of numbers, use a for loop to iterate the array and print out all the values that are smaller
# than the user input and print out all the values that are larger than the number entered by the user.

# ```
# # Start with this List
# list_of_many_numbers = [12, 24, 1, 34, 10, 2, 7]
# ```
# Example Input/Output if the user enters the number 9:
# ```
# The User entered 9
# 1  2  7 are smaller than 9
# 12  24  34  10 are larger than 9
# ```

user_num = int(input("Please enter a number: ")) # prompting user for input
list_of_many_numbers = [12, 24, 1, 34, 10, 2, 7]

#goes through each number inside the list
for eachNum in list_of_many_numbers:
    if user_num < eachNum: #compares each number to determine if user input is smaller
        print(f'User input is smaller than numbers in array: {str(eachNum)}')#prints out the smaller numbers
    elif user_num > eachNum:#compares each number to determine if user input is larger than the amount the user put in
        print(f'User input is larger than numbers in array: {str(eachNum)}')#prints out the larger number(s)