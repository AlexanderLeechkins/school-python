def write_to_file():
    user_input = ""
    loop = True
    filename = input("Please enter a filename to write to: ")
    file= open(filename, "w")
    while loop:
        answer = input("write a line: ")
        user_input += answer + "\n"
        if input("Would you like to add another line? y/n: ") == "n":
            loop = False
    file.writelines(user_input)
    file.close()

def read_file():
    filename = input("Please enter a filename to read: ")
    with open(filename, "r") as file:
        text = file.read()
        print(text)
    
user_answer=""
while user_answer != "c":  
    user_answer = input("What would you like to do\n" "-Write to a file(a)\n" "-Read from a file(b)\n" "-Exit(c)\n")
    if user_answer == "a":
        write_to_file()
    elif user_answer == "b":
        read_file()
    elif user_answer == "c":
        print("Goodbye")
    else:
        print("Invalid choice (Please select a valid option)")
