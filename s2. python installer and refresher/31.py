my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

x = 0
while x != 3: 
    for day in my_list:
        if day == "Monday":
            continue
        else:  
            print(day)
    print('\n')
    x = x + 1