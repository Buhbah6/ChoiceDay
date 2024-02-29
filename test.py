
# # print("Hello World")

# # # String
# # # any groupings of characters inside of " "
# # x = "My name is Mr. Nadeau"
# # print(x)

# # # Boolean
# # # True or False
# # x = True
# # y = False

# # if x:
# #     print("Hello")
# # else:
# #     print("World")

# # # Float
# # # Any number with a decimal point
# # x = 5.5

# # y = 5.0

# # # Integer
# # # Any whole number
# # x = 5

# # # Character / char
# # # A single character inside of '' 
# # x = 'a'

# # x = "100"
# # x = 101.0
# # x = 100000000000000000000000000000000000000000005
# # x = int(5 / 2) 

# x = 5
# x = str(x)

# x = int(x)
# x = float(x)
# x = bool(x)

# name = input("Write your name")
# print("Your name is " + name) 

# # ==
# # !=
# # >=
# # <=

# num1 = 5
# num2 = 10

# if num1 >= num2:
#     print("test1")
# elif num1 <= num2:
#     print("Test2")
# else:
#     print("test3")

# # +, -, *, /
    

firstNum = 0
secondNum = 0
operator = ""

firstNum = float(input("Please enter the first number: "))
secondNum = float(input("Please enter the second number: "))
operator = input("Please enter your operator")

if operator == "+":
    print(str(firstNum + secondNum))
elif operator == "-":
    print(str(firstNum - secondNum))
elif operator == "/":
    if secondNum != 0:
        print(str(firstNum / secondNum))
    else:
        print("The second number cannot be 0")
else:
    print("Error")

# % modulo
#    11 % 2 = 1
    
# Take 2 numbers from the user, and print if the 1st number can be evenly divided by the second number