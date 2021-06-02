from random import shuffle
print("-----------------------------------------------------------------")
print("                 Welcome to this General Knowledge Quiz")
print("-----------------------------------------------------------------")


#Ask for name by using greet function
def greet():
    global name
    while True:
        name = input("Please enter your name : ")
        if name.replace(' ','').isalpha():
            break
        print("Please only use letters to enter your name.")
greet()#calling the greet function



#Ask for age
while True:
    age = input("Please enter your age : ")
    if age.replace(' ','').isnumeric():
        break
    print("Please only use numbers to enter your name.")



#Ask if they are ready to take the quiz
status = input("Are you ready to take the quiz :{}?: \na. Yes \nb. No \n=>".format( name))


#what if the user is ready
if status == 'Yes' or status == 'yes' or status == 'Y' or status == 'y' or status == 'A' or status == 'a':
    print("Welcome to the General Knowledge quiz.")
else:
    print("Thank you trying this quiz ")
    exit()

   
##Asking if user wants instructions
def inst():
    inst = input("If you wish to read the instructions for this quiz, please press y on your keyboard :{}?: \na. Yes \nb. No \n=>")
    if inst == 'Yes' or inst == 'yes' or inst == 'Y' or inst == 'y' or inst == 'A' or inst == 'a':
     
        print("----------------------------------Instructions------------------------------------------")
        print("This quiz will ask questions based on general knowledge")
        print("There will be four possible answers for every questions")
        print("However, there will only be one correct answer for each question.")
        print("----------------------------------------------------------------------------------------")
    else:
        print("Welcome to the General Knowledge quiz")
       
                           
inst()## calling the functions
## number of questions to be asked
def rounds():
    global r
    while True:
        try:
            r = int(input("\nPlease enter how many rounds you want to play : "))##asking the user how many rounds they want to play
            if 0<r<=10:
                break
            else:
                print("please enter the rounds in 1 to 10 only")
        except:
            print('please select rounds in numbers only, also the largest amount of rounds you can enter is 10 ')



rounds()
print("                                                    ")
#set of questions that are asked
#question 1
## questions and right answers

#initial score
Q1 = 'B'
Q2 = 'B'
Q3 = 'B'
Q4 = 'B'
Q5 = 'A'

score = 0
questions=[
[
    "What is the oldest country in the world?",##Q1
    {'answer':'b','option':'\na.Japan\nb.San Marino \nc.Scotland \nd.Iceland '}
    ],

[
    "What country has the largest population?",##Q2
    {'answer':'d','option':'\na.India \nb.Brazil \nc.USA \nd.China '}
    ],


[
    "What is the largest animal in the world?",
    {'answer':'c','option':'\na.African Elephant\nb.Colossal Squid\nc.Blue Whale \nd.Brown Bear '}##Q3
    ],    
   
[
    "What is the longest river in the world?",
    {'answer':'a','option':'\na.Nile River \nb.Amazon River \nc.Yellow River \nd.Yangtze River '}##Q4
    ],    
   

[
    "In what city would you find the red square?",
    {'answer':'c','option':'\na.Tokyo \nb.Budapest \nc.Moscow \nd.Vienna '}##Q5
    ],    
     


[
    "In what century was the Mona Lisa Painted?",
    {'answer':'b','option':'\na.17th \nb.13th \nc.14th  \nd.16th '}##Q6
    ],    
     
[
    "How many stripes are there on the USA flag?",
    {'answer':'a','option':'\na.13 \nb.11 \nc.15 \nd.18 '}##Q7
    ],    

[
    "What country has the most islands in the world?",
    {'answer':'d','option':'\na.New Zealand \nb.Canada \nc.Norway \nd.Sweden '}##Q8
    ],    
[
    "In football which football club has won the most Champions leagues (formerly the European Cup)?",
    {'answer':'c','option':'\na.Bayern Munich \nb.Liverpool FC \nc.Real Madrid CF \nd.FC Barcelona '}##Q9
    ],    

[
    "What country has the longest coastline in the world?",
    {'answer': 'b','option':'\na.Norway \nb.Canada \nc.Russia \nd.Indonesia'}##Q10
    ],
]
shuffle(questions)
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
                   
r=int(input())
score=score/rounds
percentage=score*100
print(percentage)
