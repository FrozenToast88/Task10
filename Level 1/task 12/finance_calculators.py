# import math package from python then asks for user input on main question.
import math
user_inp_choose = input("Choose either 'bond' or 'investment' from the menu below to proceed : ")

# declare a if statement for bond with variations
# with the user information adding more user inputs for the required task
# bond formulars stored in variables to obtain outputs required from task
if user_inp_choose == "bond" or user_inp_choose == "Bond" or user_inp_choose == "BOND" :

# Added user inputs
    user_inp_house = float(input("Enter present value of the house : "))
    user_inp_interest = float(input("Enter interest rate : "))
    user_inp_months = int(input("Enter the number of months it will take to repay : "))

# Bond formulated variables
    bond_rate = (user_inp_interest/100)/12
    bond_formular = (bond_rate*user_inp_house)
    bond2_formular = bond_formular/(1-(1+bond_rate)**(-user_inp_months))

# declare a elif statement for investment with variations
# with the user information adding more user inputs for the required task
# investment formulars stored in variables to obtain outputs required from task
# nested if statement for the user_inp_type to gain correct output

elif user_inp_choose == "investment" or user_inp_choose == "Investment" or user_inp_choose == "INVESTMENT" :

# Added more user inputs 
    user_inp_money = float(input("Enter amount which is deposited : "))
    user_inp_perc = float(input("Enter interest rate : "))
    user_inp_year = int(input("Enter number of years planned on investing for : "))
    user_inp_type = input("Enter 'simple' or 'compound' interest rate : ")

#  investment formulated variables
    percent_intrest = (user_inp_perc / 100)
    simple_interest = (user_inp_money * (1+percent_intrest*user_inp_year))
    compound_interest = (user_inp_money * math.pow((1+percent_intrest),user_inp_year))

# nested if statement for results of user_inp_type 
    if user_inp_type == 'simple':
        print(simple_interest)
    else:
        print(compound_interest)

# if statement for bond to generate results
if user_inp_choose == "bond" or user_inp_choose == "Bond" or user_inp_choose == "BOND":
    print(bond2_formular)
else:
    print("Make sure you have followed instruction accordingly")




