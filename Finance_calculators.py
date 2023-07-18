                # Finance calculators program
                
# import math calculator
import math

# create calculator selection function
# display math calculators
# get user input for calculator of choice              
def investment_selector():
    print("")
    calculator_choice = input(" investment - to calculate the amount of interest you'll earn on your investment:\n\n bond -\t to calculate the amount you'll have to pay on a home loan:\n\n Enter 'INVESTMENT' or 'BOND' from the menu above to proceed: ").lower()

    # diplay error if wrong choice made
    # reinitialize function if condition not met
    # print selected calculator

    if (calculator_choice != "investment") and (calculator_choice != "bond"):
        print("")
        print(" ERROR:\t please select a valid option from above:\n INVESTMENT OR BOND!")  
    while (calculator_choice != "investment") and (calculator_choice != "bond"):
        return(investment_selector())
    print(f"\n You have selected {calculator_choice.upper()} as your calculator of choice: ")

    # get input for investment finance calculation
     
    if calculator_choice == "investment":
        p = float(input("\n Please enter the amount you wish to deposit today:\t "))
        r = float(input(" Please enter your interest rate:\t"))
        t = float(input(" please enter the amount of years for investment:\t "))
 
        # equation for simple interest
        # equation for compound interest
        # get user input for simple or compound interest
        # create loop for incorrect response
        
        simp_total = (r/100*p*t)
        A = round(p*(1 + r/100*t))
        comp_total = (p * math.pow((1+r/100),t)-p)
        a = int(p * math.pow((1+r/100),t))
        interest = input(" Please specify your interest type:\t 'simple' or 'compound': ").lower()
        print(" Thank you! ")
        while (interest != "simple") and (interest != "compound"):
            interest = input(" Error specify your interest type:\t 'simple' or 'compound': ").lower()

        # display equation for user choice

        if interest == "simple":
            print(f"\n you have selected: {interest} interest to be applied\n")
            stat_1 = (f"\n intrest rate : {r}%\n total investment : £{A}\n total duration : {t} years\n total interest : £{simp_total}\n\n### Thank you for using this calculator! ###")
            print(stat_1)
        if interest == "compound":
            print(f"\n you have selected: {interest} interest to be applied\n")
            stat_2 = (f"\n intrest rate : {r}%\n total investment : £{a}\n total duration : {t} years\n total interest : £{comp_total}\n\nThank you for using this calculator!")
            print(stat_2)

    # get user input for bond statment and print results also as dictionary

    def bond():
        if calculator_choice == "bond":
            P = float(input(" please input the present value of your house : "))
            i = float(input(" please enter your interest rate : "))
            m = (i / 100 / 12)
            n = float(input(" please input the number of months you would like your repayment plan : ")) 
            repayment = int(round(m * P) / (1 - (1 + m )**(-n)))
            interest_total = (repayment * n - P)
            total_loan = (repayment * n)
            stat_3 = (f"\n monthly repayment : £{repayment}\n\n interest rate : {i}% \n\n loan duration : {n} months\n\n total interest payable : £{interest_total}\n\n total repayable : {total_loan}  ")
            print(stat_3)
            print("")
            print("Thank you for using this calculator!\n\n")
            bond_dict = {" BOND CALCULATION":"", 
                        " monthly repayment" : f"£ {repayment}",
                        " interest rate" : f"{i} %",
                        " loan duration " : f"{n} months",
                        " total interest payable" : f"£{interest_total}"}
            for keys, values in bond_dict.items():
                print(keys, ":" ,values)

    # reload calculator option

    def re_sel():
          reload = input("\nwould you like to reload the investments calculator? y/n : ").lower()
          if reload == "y":
              investment_selector()
          if reload == "n":
              print("\nThanks for using our calculator\n####### Good Bye! ####### ")
              quit()
          else:
              print("\nError Please Retype correct characters\n")
              re_sel()

    bond()
    re_sel()
       
investment_selector()



    







