tasks=[]

def addtask():
    task=input("what task do you want added ")
    tasks.append(task)
    print("task added")

def showall():
    for task in tasks:
        print(task)
    if len(tasks)==0:
        print("no tasks")
    
def Check_next_task():
    if len(tasks) != 0:
        print (f"Your next task is: {tasks[0]}")
    else:
        print("no tasks")
        
def complete_next_task():
    tasks.remove(tasks[0])   
    print("your first item has been removed") 

def quit_program():
    print("goodbye")

print("Options:")
print("1. Add a task")
print("2. Display all tasks")
print("3. Check the next task")
print("4. Complete the next task")
print("5. Quit")

userinput= int(input("what task would you like to do "))
while userinput != 5:
    if userinput ==1:
        addtask()
        userinput= int(input("what task would you like to do "))
    elif userinput ==2:
        showall()
        userinput= int(input("what task would you like to do "))
    elif userinput ==3:
        Check_next_task()
        userinput= int(input("what task would you like to do "))
    elif userinput ==4:
        complete_next_task()
        userinput= int(input("what task would you like to do "))
    elif userinput ==5:
        quit_program()
    else:
        print("Invalid input, please enter a number 1-5")
        break
    