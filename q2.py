# ### Problem 2
# Prompt the user with the message, ‘Is it better to be rude or kind to People?’ 
# Keeping prompting the user to enter an answer until they enter the word kind. 
# Each time they enter something other than kind, print the message, ‘That’s not the answer I had hoped to hear. Try again.’ and prompt the user again.
# Once the user enters kind, print, ’Now that’s what I wanted to hear!’ and exit the program.

user_input = input("Is it better to be rude or kind to People? Enter 'kind' to quit.")# ask user for input
while (user_input != 'kind'): #if user input is not equal to kind the loop will run
    if user_input != 'kind': #user input is the false case this code will run
        print("That’s not the answer I had hoped to hear. Try again.")
    elif user_input == 'kind':#user input is the true case this code will run
        print("Now that’s what I wanted to hear!")
    user_input = input("Is it better to be rude or kind to People? Enter 'kind' to quit.")#user prompted again to either provide another answer or exit loop