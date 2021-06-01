#this program is for the scoring mechanics for the quiz
## score mechanics
print("Main Routine")
while r>0:
    data = questions[0]
    q = data[0]
    data =data[1]
    answer = data['answer']
    option = data['option']

    print(q)
    print(option)
    while True:
        user_answers = input("Please enter your answer here : ").lower().replace(' ','')
        if user_answers =='a' or user_answers == 'b' or user_answers == 'c' or user_answers == 'd':
            if user_answers == answer:
                print("***************************")
                print("Well done!, you got the correct answer ")
                print("***************************")
                score +=1
                print("-------")
                print("your score is",score)
                print("-------")
            else:
                print("**********************************************************")
                print("Sorry, that is the incorrect answer. The correct answer was ",answer)    
                print("**********************************************************")
                print("-------")
                print("your score is",score)
                print("-------")


            del questions[0]
            r-=1
            break
        else:
            print("Please enter the alphabet for the chosen option")
