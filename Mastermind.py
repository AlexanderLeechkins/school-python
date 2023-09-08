import random
num1 = random.randint(0,5)
num2 = random.randint(0,5)
num3 = random.randint(0,5)
num4 = random.randint(0,5)

userinput1= int(input("whats the first number you are guessing "))
if num1 == userinput1:
    print("good work you got the first number correct")

userinput2= int(input("whats the second number you are guessing "))
if num2 == userinput2:
    print("good work you got the second number correct")

userinput3= int(input("whats the third number you are guessing "))
if num3 == userinput3:
    print("good work you got the third number correct")

userinput4= int(input("whats the fourth number you are guessing "))
if num4 == userinput4:
    print("good work you got the fourth number correct")

