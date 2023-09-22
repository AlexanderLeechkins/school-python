name_list = ['Ed', 'William', 'Toby', 'Freddie', 'Rohan', 'Ian', 'Matthew', 'Gavin', 'Lenny', 'Thomas', 'Jake']
new_names = []
for i in range(3):
    new_name = input("Enter a name: ")
    new_names.append(new_name)
name_list.extend(new_names)
print("The entire list of names is:", name_list)
print("The third name is:", name_list[2])
print("The last seven names are:", name_list[-7:]) 