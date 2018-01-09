#File: credit_adupree.py
#Description: Tells user if their credit limit is exceeded
#Author: Alex DuPree, Alex Hoang
#Date: 10/16/2017
#Compiler: 3.4.1

print("This program will tell the user if they have exceeded their credit"
      "limit for the month")


def main():
    acct_num = int(input("\nAccount number? "))
    if acct_num <= 0:
        print("\nInvalid account number, positive integers only.")
        exit()
    
    balance = float(input("\nBalance at the beginning of the month? "))

    total_charged = float(input("\nTotal of all items charged by the customer this month? "))
    if total_charged <= 0:
        print("\nInvalid charge amount, positive integers only.")
        exit()
        
    credits_applied = float(input("\npayments made to account this month?"))
    if credits_applied <= 0:
        print("\nInvalid credits applied, positive itegers only.")
        main()
    
    credit_limit = float(input("\nTotal credit limit? "))
    if credit_limit <= 0:
        print("\nInvalid credit limit, positive integers only.")
        exit()

    balance = balance - credits_applied + total_charged

    if balance >= credit_limit:
        print("\nYou have exceeded your credit limit for account {} by {} USD"
              .format(acct_num, (balance - credit_limit)))
    else:
        print("\nfor account {} you have {} USD Left to spend."
              .format(acct_num, (credit_limit - balance)))


main()

    
