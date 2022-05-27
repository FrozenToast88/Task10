usern = []
passw = []

register = open("user.txt", "r+")
lines = register.readlines()

for line in lines:
    remove = line.strip().replace(" ", "").split(",")
    print(remove)
    usern.append(remove[0])
    passw.append(remove[1])




def reg_user():
        if userName == "admin":
            new_usern = input("Enter new username : ")
            register = open("user.txt", "r+")

            newUser = False
            while newUser == False:
                if new_usern in usern:
                    print("This username arleady exist please try again! ")
                    new_usern = input("Enter new username : ")

                else: 
                    newUser = True
            
            while newUser == True:
                new_passw = input("Enter new password : ")
                con_passw = input("Confirm new password : ")

                if new_passw != con_passw:
                    print("New password and confirm new password does not match!")
                    con_passw = input("Confirm new password : ")


                elif new_passw == con_passw:
                    usern.append(new_usern)
                    passw.append(con_passw)
                    login_newDetails = ("\n" + str(new_usern) + ", " + str(con_passw))
                    register.write(login_newDetails)
                    newUser = False


# add_task() method
# user input requested
# data captured writen to task.txt

def add_task():
    from datetime import datetime
    
    task_userName = input("Enter task username : ")
    task_title = input("Enter the title of your task : ")
    task_descr = input("Enter task description : ")
    # I obtained this function through research on a website
    # this allows me to obtain current date
    # website:URL:https://speedysense.com/get-current-date-time-python
    current_date = datetime.now().date()
    task_dueDate = input("Enter due date exp: yyyy/mm/dd :  ")
    task_completed = ("No")
    task_info = open("tasks.txt", "a+")
    task_info.write("\n" + task_userName+ ", " +task_title+ ", " +task_descr+ ", " +str(current_date)+ ", " +task_dueDate+ ", " +task_completed)
    task_info.close()



# view all method
# this for statement loops through data in task_info allow us to call specific data
# remove2 changes the data read from task.txt into a list format to be able to manage and call data more efficiently
# this print statement contains concatenated data of specific data by using index thats called from tasks text document for all users

def view_all():
    task_info = open("tasks.txt", "r")
    taskLine = task_info.readlines()
    for line in taskLine:
        remove2 = line.strip().split(", ")
        print("Task :               "+ str(remove2[1]))
        print("Assigned to :        "+ str(remove2[0]))
        print("Date assigned :      "+ str(remove2[3]))
        print("Date due :           "+ str(remove2[4]))
        print("Task Complete? :     "+ str(remove2[5]))
        print("Task description :\n "+ str(remove2[2]))
    
    task_info.close()

# view_mine method
# this for statement loops through data in task_info allow us to call specific data
# this print statement contains concatenated data of specific data by using index thats called from tasks text document for only logged in user
# close task_info document

def view_mine():
    count = []
    x = 0
    task_info = open("tasks.txt", "r")
    read = task_info.readlines()
    all_count = -1
    for line in read:
        all_count += 1
        temp = line.strip().split(",")
        if temp[0] == userName:
            x += 1
            
            count.append(all_count)
            print("Task nr :             "+ str(x))
            print("Task :               "+ str(temp[1]))
            print("Assigned to :         "+ str(temp[0]))
            print("Date assigned :      "+ str(temp[3]))
            print("Date due :           "+ str(temp[4]))
            print("Task Complete? :     "+ str(temp[5]))
            print("Task description :\n "+ str(temp[2]))
            print(count)


            
    task_num = int(input("Enter task number you want or -1 to Exit : "))
    if task_num == -1:
        return
    
            
    task_num2 = task_num - 1
    view_task = count[task_num2]
    print(view_task)
    print(read[view_task])

    
    
    taskComplete = input("mark the task or edit the task /exp : 'mark' or 'edit' : ")
    taskComplete2 = taskComplete.lower().strip().replace(" ", "")



    if taskComplete2 == "mark":
        shatter = read[view_task].split(",")
        edit = read[view_task].replace("No", "Yes")
        read[view_task] = (f"{edit}")
        print(read[view_task])



        
        
    
    if taskComplete2 == "edit":
        shatter = read[view_task].split(",")
        if shatter[5] in shatter != "Yes":
            option2 = input("would you like to edit 'assigned' or 'due date' : ")
            option2Alpha = option2.lower().replace(" ","")
            if option2Alpha == "assigned":
                usern_edit = input("Enter new assigned username : ")
                read[view_task] = (f"{usern_edit}, {shatter[2]}, {shatter[3]}, {shatter[4]}, {shatter[5]}")
                print(read[view_task])
                
                
                
            
            if option2Alpha == "duedate":
                duedate_edit = input("Enter new due date /exp : yyyy-mm-dd : ")
                read[view_task] = (f"{shatter[0]}, {shatter[1]}, {shatter[2]}, {shatter[3]}, {duedate_edit}, {shatter[5]}")
                print(read[view_task])
        else:
            print(f"{userName} task already has been marked! ")         
        
    
# ensuring rewrite of the data in task.txt regardless has there been no changes
    beta = open("tasks.txt","w")
    for x in read:
        beta.write(str(x))


    beta.close()
    task_info.close()
    

# task_overview method
# import datetime to compare dates for overdue results
# reading data from task.txt
# if statements requesting complete,incomplete and over due tasks 
def task_overview():
    from datetime import datetime
    task_info = open("tasks.txt", "r")
    read = task_info.readlines()
    completed_tasks = 0
    incompleted_tasks = 0
    over_due = 0
    all_count = -1
    for line in read:
        all_count += 1
        temp = line.strip().split(",")
        datesplit = temp[3].split("-")
        datesplit2 = temp[4].split("-")
        
        if temp[5] == " Yes":
                completed_tasks += 1
        if temp[5] == " No":
                incompleted_tasks += 1

                # convert String data to integer to be compatible with datetime 
                date1 = datetime(int(datesplit[0]),int(datesplit[1]),int(datesplit[2]))
                date2 = datetime(int(datesplit2[0]),int(datesplit2[1]),int(datesplit2[2]))
                if date1 > date2 :

                    over_due += 1
               
    one_more = all_count + 1

    # calculations
    perc_taskInc = round((( incompleted_tasks / one_more ) * 100), 1)
    perc_taskOve = round(((over_due / all_count) * 100), 1)
    
    # display results
    print("task_overview : ")
    print(f"Total amount of tasks                    : {one_more}")
    print(f"Total amount of complete tasks           : {completed_tasks}")
    print(f"Total amount of incomplete tasks         : {incompleted_tasks}")
    print(f"Total amount of over due tasks           : {over_due}")
    print(f"Total percentage of tasks incomplete     : {perc_taskInc}%")
    print(f"Total percentage of tasks over due       : {perc_taskOve}%")
    print(" ") 
        

    # write data calculated and captured to task_overview 
    test2 = open("task_overview.txt","w")
    with test2:
        
        test2.write(f"Total amount of tasks                    : {one_more}")
        test2.write(f"\nTotal amount of complete tasks           : {completed_tasks}")
        test2.write(f"\nTotal amount of incomplete tasks         : {incompleted_tasks}")
        test2.write(f"\nTotal amount of over due tasks           : {over_due}")
        test2.write(f"\nTotal percentage of tasks incomplete     : {perc_taskInc}%")
        test2.write(f"\nTotal percentage of tasks over due       : {perc_taskOve}%")    
        
        
    task_info.close()
    test2.close()





# import datetime to compare dates for overdue results
# reading data from user.txt & task.txt
# if statements for each user requesting complete,incomplete and over due tasks and task count

def user_overview():
    from datetime import datetime
   

    taak = open("user.txt","r")
    task_info = open("tasks.txt", "r")
    read = task_info.readlines()
    lees = taak.readlines()


    user_count = len(lees)
    task_count = len(read)
    
    all_count = -1
    completed_tasks = 0
    incompleted_tasks = 0
    over_due = 0
    user_taskAm = 0
    persons_task = [] # store users indiviual tasks / this will run for each user 

   
        
       


    test = open("user_overview.txt","w") # wipe text file for new data to be captured
    for i in usern:
        persons_task = []
        

        for line in read:
           
            
            temp = line.strip().split(", ")
            datesplit = temp[3].split("-")
            datesplit2 = temp[4].split("-")
            
        
            
            
            if temp[0] == i:
                user_taskAm += 1
                persons_task.append(line)
                persons_total = len(persons_task)
                
                
                all_count += 1
                
                
               
    
                if temp[-1] == "Yes":
                    completed_tasks += 1
                    
                        
                if temp[-1] == "No":
                    
                    incompleted_tasks += 1
                    # convert string data to integer then datas are compared to each other
                    date1 = datetime(int(datesplit[0]),int(datesplit[1]),int(datesplit[2]))
                    date2 = datetime(int(datesplit2[0]),int(datesplit2[1]),int(datesplit2[2]))
                    if date1 > date2 :
                        over_due += 1
        

                # calculations for percentages
                perc_taskCom = round(((completed_tasks / persons_total) * 100), 1)
                perc_taskInc = round(((incompleted_tasks / persons_total) * 100), 1)
                perc_taskOve = round(((over_due / persons_total) * 100), 1)
                perc_taskUser = round(((user_taskAm / user_count) * 100), 1)


        # if statement needed to allow certain data to only be displayed once
        if all_count == 0 or all_count == 1:
            print("user_overview : ")
            print(f"Total number of users : {user_count}")
            print(f"Total number of tasks : {task_count}")
            print(f"\n{i} statistics : ")
            print(f"{i} percentage of tasks complete : {perc_taskCom}%")
            print(f"{i} percentage of tasks incomplete : {perc_taskInc}%")
            print(f"{i} percentage of tasks incomplete and over due : {perc_taskOve}%")
            print(f"{i} percentage of tasks of total tasks : {perc_taskUser}%")
            print(" ")  




        elif all_count > 1:
            print(f"\n{i} statistics : ")
            print(f"{i} percentage of tasks complete : {perc_taskCom}%")
            print(f"{i} percentage of tasks incomplete : {perc_taskInc}%")
            print(f"{i} percentage of tasks incomplete and over due : {perc_taskOve}%")
            print(f"{i} percentage of tasks of total tasks : {perc_taskUser}%")
            print(" ")  

            

            

        
            
        # write all data to user_overview
        test = open("user_overview.txt","a+")
        
        with test:
                # if statement needed to allow certain data to only be displayed once
                if all_count == 0 or all_count == 1:
                    test.write(f"Total number of users : {user_count}")
                    test.write(f"\nTotal number of tasks : {task_count}")
                    test.write(" ")
                    test.write(f"\n{i} statistics : ")
                    test.write(f"\n{i} percentage of tasks of total tasks : {perc_taskUser}%")
                    test.write(f"\n{i} percentage of tasks complete : {perc_taskCom}%")
                    test.write(f"\n{i} percentage of tasks incomplete : {perc_taskInc}%")
                    test.write(f"\n{i} percentage of tasks incomplete and over due : {perc_taskOve}%")

                elif all_count > 1:    
                    test.write(f"\n{i} statistics : ")
                    test.write(f"\n{i} percentage of tasks of total tasks : {perc_taskUser}%")
                    test.write(f"\n{i} percentage of tasks complete : {perc_taskCom}%")
                    test.write(f"\n{i} percentage of tasks incomplete : {perc_taskInc}%")
                    test.write(f"\n{i} percentage of tasks incomplete and over due : {perc_taskOve}%")
            

        user_taskAm = 0
        completed_tasks = 0
        incompleted_tasks = 0
        over_due = 0
            
        


    test.close()
    taak.close()
    task_info.close()

    
        
    

        



# importing datetime allowed me to call certain functions as datetime.now().date()
from datetime import datetime
# Registers the username and password in user.txt
# empty lists 
# open user text document read and write functions applicable
# gear while True allows loop to continue until False
# check while True allows the code to loop through login in user input request until results are obtained
# read lines of user text document
# for loop in lines variable which cont tains user.txt read lines
# each time line loops in through lines it strips replaces synax and splits via a specific syntax
# each data effected by remove variable loops through lines variable and appends a specific character shown by index 
# which will be placed into the empy lists at the begining 

check = True

usern = []
passw = []
print("Welcome to task_manager")
print("Login Information : \n")
register = open("user.txt", "r+")
lines = register.readlines()

for line in lines:
    remove = line.strip().replace(" ", "").split(",")
    usern.append(remove[0])
    passw.append(remove[1])
userName = input("Enter Username : ")
passWord = input("Enter Password : ")
while check:
# as per review changed 'and' to 'or' 
    if userName not in usern or passWord not in passw:
        print("Invalid user information..try again! ")
        print("Login Information : \n")
        userName = input("Enter Username : ")
        passWord = input("Enter Password : ")
    else:
        check = False

# contains requirements of task 2
# Initail if statement which goes through lists to check who is loging in
# f string allowing us to call varaibles as we please

# as per review when logining in as admin options would not run so i placed everything to do with the option in the while loop that holds admin
while check == False:
    if userName in usern and passWord in passw and userName == "admin":
        print(f"Welcome {userName}\n")
# requested input which contains the options which admin will only see.
# task 2 request
        option = input("Please select one of the following options : \nr - register user \na - add task \nva - view all tasks \nvm - view my task \ngr - generate reports \nds - display statistics \ne - exit \nEnter your option here :").lower()
        
    elif userName in usern and passWord in passw:
            print(f"Welcome {userName}\n")
    
            option = input("Please select one of the following options : \nr - register user \na - add task \nva - view all tasks \nvm - view my task \ne - exit \nEnter your option here :").lower()

# this if statement contains the variable option which contains data that we need to allow the code to run accourding to the data.
# requested input to reregister user data.
# if requirements are met the data will be appended to the the lists containing the registery data
# write the new user data into user.txt 
    if option == "r":
        reg_user()
 


# this if statement run code when requirements are met "a" raviation
# call add_task() method
    if option == "a":
        add_task()      
        




# this if statement run code when requirements are met "va" raviation
# calls view_all() method containing data requested
    if option == "va":
        view_all()
       


# this if statement run code when requirements are met "vm" raviation
# calls view_mine() method containing data requested
    if option == "vm":
        view_mine()
       
# the option to view gerenal reports is private to admin
# calls task and user overview which contains data requested
    if option == "gr" and userName == "admin":
        task_overview()
        user_overview()

        
# this if statement run code when requirements are met "va" raviation and is exclusive to the user "admin"
# this print statement contains a concatanated data and specific data from the list in the begining in numerical form
# open tast.txt to call data so that we read and manipulate them
# we needed a interge variable to be called in the for loop
# this for loop runs through each line and adds a 1 to line allowing us to get the total amount of tasks
    if option == "ds" and userName == "admin":
        print("Total number of users : " + str(len(usern)))
        task_info = open("tasks.txt", "r")
        taskLine = task_info.readlines()
        line = 0
        for line in range(len(taskLine)):
            line += 1
        print("Total number of Tasks : "+ str(line))




# this if statement when requirments are met it will exit the user out of the program
# obtained the knowledge of exit() from lecturor
# gear turns false when option 'e' is prompt
# close user.txt document
    if option == "e" or option == "E":
    
        exit()
    register.close()

        
else:
    print("Invalid user information ")
