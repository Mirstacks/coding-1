# 1. A company is developing a security system that requires 2 factor 
# authorization. This means that the system needs to verify 
# that 2 pieces of data are correct for the
# person to enter the building. When someone 
# approached the building they need to have the correct 
# name and correct passcode to enter the building. 
# Which operator would be used here? Please provide a code 
# example of how you would write this and output the 
# result using the print() function for python or the console.log() function for javascript? 

name = 'Samir'
password ='Samir2024'

securitySystemName ='Samir'
securritySystemPassword='Samir2024'

print(name == securitySystemName and password == securritySystemPassword)

# 2. A hospital needs to keep track of medical equipment. 
# they are getting a shipment of new ECG machines and Oxygen 
# tanks and need to verify. If they have more than whats needed 
# in their office, they need to send the overflow of e
# quipment back to the manufacturer, but if they have less, 
# they need to request more.
# In this scenario, they are supposed to have 
# 10 ECG machines, but only recieved 4, and 
# for the oxygen tanks they are supposed to have 6 in stock, 
# but recieved 9. 
# Which operator would be used here? 
# Please provide a code example of how you would 
# write this and output the result using the print() 
# function for python or the console.log() function for javascript? 
ecgRequest = 10
ecgShipment = 4
oxygenRequest = 6
oxygenShipment = 9

# You would use Comparion operator 

# 3. A company is developing a messaging app that 
# allows people to send text message for free. They need 
# to allow users to capture the user data and then send it 
# to someone else. Which operator would be used here? Please 
# provide a code example of how you would write this and 
# output the result using the print() function for python 
#or the console.log() function for javascript? 

# You would use the assignment operator
senderMsg ='Hello friend'
recieverMsg = senderMsg
print(recieverMsg)

# ## for student's learning Python
# 4. Use W3 schools to research the input function. then create 2 
# variable that will contain the values/ data from your inputs. 
# The data you pass in should be your name and your age. 
# Lastly, use string concatenation to combine the new 
# variable you created with the sentence below.

# for students learning Python
# print('my name is' + name '.  I am ' + age + 'years old.' )
print("Enter your name:")
x = input(my name is)
y = input(Samir)
z = input("I am")
age = input(16 years old)
print("Hello, " + x + y + z + age )
