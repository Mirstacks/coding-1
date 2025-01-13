# 1. Create a function that will determine if a number passed into it's funtion parameters is either positive or negative.
# For example, If I pass in the number 10 it should return the message,"this  is a positive number", or if I type in the number 
# -12, it should return the message, "this is a negative number. If the user types in zero, it should return the message
# "this is zero".

def check_number(num):
    if num > 0:
        return "This is a positive number."
    elif num < 0:
        return "This is a negative number."
    else:
        return "This is zero."

print(check_number(10))   
print(check_number(-12))
print(check_number(0))   

# 2. You have been hired by netflix to help them develop a movie ticket program. You must create a function that will check
# the movie goers age and return the price of the movie ticket based on that person's age. Provided are the lists of ages 
# and the prices:

# - 10 and under should pay $5.00
# - 16 and up should pay $10.00
# - 20 an up should pay $15.00
# - 65 and up should pay 5.00

def movie_ticket_price(age):
    if age <= 10:
        return "$5.00"
    elif age >= 16 and age < 20:
        return "$10.00"
    elif age >= 20:
        return "$15.00"
    elif age >= 65:
        return "$5.00"
    

# Test the function
print(movie_ticket_price(8))   # Output: $5.00
print(movie_ticket_price(16))  # Output: $10.00
print(movie_ticket_price(18))  # Output: $10.00
print(movie_ticket_price(22))  # Output: $15.00
print(movie_ticket_price(70))  # Output: $5.00


# 3. You have been hired by target to assist them with their store member discount software. The would like to make it 
# so that shoppers who have a specific membership tier can save a certain amount of money on the products they buy. 
# provided below are the memberships and the discount amount they should recieve:

# - superShopper should recieve a 10% discount on their items
# - megaShopper  should recieve a 15% discount on their items
# - ultraShopper should receive a 20% discount on their items

# You program should be able to take in the shoppers membership type, the name of the item they are purchasing, and the 
# item price, and should return a message telling the user what the final price of the item is and how much they saved.

# For example: congratulations superShopper, you saved $10.00 on this TV. Your final
# item price is $90.00. 

def calculate_discount(membership, item_name, item_price):
    # Define discount rates for each membership type
    if membership == "superShopper":
        discount_rate = 0.10
    elif membership == "megaShopper":
        discount_rate = 0.15
    elif membership == "ultraShopper":
        discount_rate = 0.20
    else:
        return "Invalid membership type."

    # Calculate discount amount and final price
    discount_amount = item_price * discount_rate
    final_price = item_price - discount_amount

    # Return the message with the result
    return (f"Congratulations {membership}, you saved ${discount_amount:.2f} on this {item_name}. "
            f"Your final item price is ${final_price:.2f}.")

print(calculate_discount("superShopper", "TV", 100))  
print(calculate_discount("megaShopper", "Laptop", 200))  
print(calculate_discount("ultraShopper", "Phone", 500))  
print(calculate_discount("basicShopper", "Tablet", 150))  
