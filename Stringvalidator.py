import re

def validate_number(Stringinput):
    patterns= r"^\d{1,3}(,\d{3})*\.\d{2}$"
    if re.match(patterns, Stringinput):
        print("valid")
    else:
        print("not valid")        
    
hi=1
while hi==1:
    stringinput=(input("what string would you like to test(or quit) "))
    validate_number(stringinput)
    if stringinput== "quit":
        break
     
