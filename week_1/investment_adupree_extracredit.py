#File: investment_adupree_extracredit.py
#Description:Computes the future investment value though compound interest
#Author:Alex DuPree
#Date: 10/06/2017
#Compiler: 3.4.1

#Poll user for initial investment value, monthly rate, and number of years
investment = float(input("Initial investment amount? "))
rate = float(input("Monthly rate as a percentage? "))
years = float(input("Number of years to be compounded? "))
#Uses compound interest formula to find future invest value
future_investment = investment * (1 + (rate/100))**(years*12)
#Prints final investment value to display
print("An investment of {} USD at a monthly rate of {}% over {} year(s) will be {} USD".format(investment, rate, years, future_investment))
      
