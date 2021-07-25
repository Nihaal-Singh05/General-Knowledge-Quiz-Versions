## number of questions to ask the user
def rounds():
    global r
    while True:
        try:
            r = int(input("\nPlease enter how many rounds you would like to play : "))##asking the user how many rounds they want to play
            if 0<r<=10:
                break
            else:
                print("please enter the rounds in 1 to 10 only")
        except:
            print('please select rounds in numbers only, also the largest amount of rounds you can enter is 10")')
rounds()
