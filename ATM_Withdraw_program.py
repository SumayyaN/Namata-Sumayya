
#Exercise three
print("Welcome to my Atm\n")
print("chooose an option to countinue \n 1.Withdraw(1)\n 2.Exit(2)")

Balance = 50000
while True :
    choice = int(input("Enter an option :\n"))
    if choice == 1 :
        taken = int(input("Enter the amount you want to withdraw\n"))
        if taken <= Balance :
            Balance = Balance - taken 
            print("Withdrawal successful.")
            print("Your new balance is:", Balance)
        else:
            print("Insufficient balance.")
            
    elif choice == 2:
        print("Have a nice day")
        break
        
    else:
        print("Enter a valid option (1 or 2)")
        