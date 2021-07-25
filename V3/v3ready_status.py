def status():
    while True:
        status = input("Are you ready to take the quiz (Enter Yes or No) :{}?: \na. Yes \nb. No \n=>".format( name)) 
        if status == 'Yes' or status == 'yes' or status == 'Y' or status == 'y' or status == 'A' or status == 'a' or status == 'YES' or status == '1':
            print("Welcome to the General Knowledge quiz.")
            break
        if status == 'No' or status == 'no' or status == 'N' or status -- 'n' or status == 'B' or status == 'b' or status == 'NO' or status == '2':
            print("Thank you trying this quiz ")
            exit()

status()
