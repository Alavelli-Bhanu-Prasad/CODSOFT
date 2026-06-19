import random 
import string 
Password_length=int(input("Enter the length of the password: "))    #Define the length of the password
Lower_case=string.ascii_lowercase
Upper_case=string.ascii_uppercase
symbols=string.punctuation
Mixed_Pass=Lower_case+Upper_case+symbols   # combine all the characters 
Password=""
for i in range(Password_length):
    Password +=random.choice(Mixed_Pass)   # Generation logic
print(Password)   # Print the output