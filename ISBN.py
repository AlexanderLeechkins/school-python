for numbers in range(1,13):
    userinput= int(input("please enter next digit of ISBN "))
    isbn=[]
    isbn.append(userinput)
    break

CalculatedDigit= 0
count=1

while count <12:
    CalculatedDigit= CalculatedDigit+ isbn[count]
    count = count+1
    CalculatedDigit= CalculatedDigit + isbn[count] * 3
    count=count+1
    break

while CalculatedDigit >= 10:
    CalculatedDigit= CalculatedDigit- 10
    break

CalculatedDigit= 10- CalculatedDigit
if CalculatedDigit ==10:
    CalculatedDigit=0

if CalculatedDigit== isbn[13]:
    print("valid ISBN")
else:
    print("invalid ISBN")












