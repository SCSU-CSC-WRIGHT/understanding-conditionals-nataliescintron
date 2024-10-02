#Temperature Check
temp_c = float(input('Enter the current temp: '))

if temp_c > 30:
    print( "It's a hot day.")
else:
    print("The weather is cool.")

#Number Comparison
num_1 =  int(input('Enter in your first number: '))
num_2 = int(input('Enter in your second number: '))

if (num_1 > num_2):
    print(num_1)
elif(num_2 > num_1):
    print(num_2)
else:
    print("They're equal!")


#Password Checker
admin_pass = "Adminpass123"
user_pass = input("Enter a password: ")

if user_pass != admin_pass:
    print("Access Denied.")
else:
    print("Access Granted.")

#Simple Calculator
x = int(input("Enter in a number: "))
y = int(input("Enter in a number: "))
op = input("Enter an OP: ")
if (op =='+'):
    print(x + y)
if (op =='-'):
    print(x - y)
if (op =='*'):
    print(x * y)
if (op =='/'):
    print(x/y)


#Positive, Negative, Zero
number = int(input("Enter a number: "))
if number > 0:
    print("Your number is positive.")
elif number < 0:
    print("Your number is negative.")
else:
    print('Your number is zero.')

#Day of the Week -  hehe I used a list
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

user_input = int(input("Enter a number from 1-7: "))

if user_input == 1:
    print(days[0])
elif user_input == 2:
    print(days[1])
elif user_input == 3:
    print(days[2])
elif user_input == 4:
    print(days[3])
elif user_input == 5:
    print(days[4])
elif user_input == 6:
    print(days[5])
else:
    print(days[6])