
# 1. Create a function that will accept a word in the function parameter
# and return the word in reverse order.
# For example, the word 'pet' should return as 'tep', the word 'book'
# should return as 'koob', etc.
# HINT- There is a built-in function that you can use to accomplish this. 
# Please use W3 schools to research what function you'll need to use.

# Function to reverse a word
txt = "bowl"[::-1]
txt2 = "book"[::-1]

print(txt)
print(txt2)

# 2. Create a function that uses a conditional statement to output a block
# of text that will tell users about a states landmarks.
# Your program should return the following states and their respective
# landmarks. For example, if a user passes in the value of south carolina,
# in the function parameter, your program should return the message:
# ' A landmark in South Carolina is Fort Sumter, where the inital shots of the'
# 'American Civil war took place.' WRITE A COMPLETE SENTENCE!

# Pennsylvania = Liberty Bell.
# New York = Statue of Liberty.
# California = Hollywood Walk of Fame.
# One additional state and landmark of your choice.

# If you pass in a state that does not exist in your program,
# your function should return a message saying that the state
# could not be found.

def state_landmark(state):

    if state == "Pennsylvania":
        return "A landmark in Pennsylvania is the Liberty Bell."
    elif state == "New York":
        return "A landmark in New York is the Statue of Liberty."
    elif state == "California":
        return "A landmark in California is the Hollywood Walk of Fame."
    elif state == "Paris":
        return "A landmark in Paris is the Effiel Tower."
    else:
        return f"Sorry, the state '{state}' could not be found."

# Test the function
print(state_landmark("Pennsylvania"))  
print(state_landmark("California"))   
print(state_landmark("New York"))
print(state_landmark("Paris"))  
print(state_landmark("China"))      

# HINT: refer back to your notes and use w3schools to reseach if/else conditional statements.