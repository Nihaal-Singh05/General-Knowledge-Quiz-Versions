# This is a simple quiz based on general knowledge 
# Initial score

correct = 0
score = 0
incorrect = 0

# Ask For Name
while True:
    name = input("Enter Your Name : ")
    if name.isalpha():
        break
    print("Please Only Enter Letters")

# Ask For Age
while True:
    age = (input("Please Write Your Age : "))
    if age.isnumeric():
        break
    print("Please Only Enter Numbers")


#Ask If User Knows How To Play
knowing = input("Do you know how to play the quiz?: {}?: \na. Yes \nb. No \n=>".format(name))

#What If The User Does Not Know How To Play
if knowing == 'No' or knowing == 'no' or knowing == 'B' or knowing == 'b' or knowing == 'N' or knowing == 'n' :
    print("This quiz will ask you questions about the subject of sports")
    print("There will be one correct answer per question. Each Question will have")
    print("four possible answers for each question.")
    print("You can answer the question by writing your chosen answer or the letter representing that answer.")

# What if the user Knows How To Play The Game?
elif knowing == 'Yes' or knowing == 'Yes' or knowing == 'A' or knowing == 'a' or knowing == 'y' or knowing == 'Y' :
    print("Welcome To The Quiz.")

#Ask If They Are Ready To Take The Quiz
status = input("Are You Ready To Take The Quiz? : {}?: \na. Yes \nb. No \n=>".format(name))

# What if the user is not ready
if status == 'No' or status == 'no' or status == 'B' or status == 'b' or status == 'n' :
    print("Thats alright, See You Next Time.")

# What if the user is ready?
elif status == 'Yes' or status == 'yes' or status == 'A' or status == 'a' or status == 'y':
    print("Welcome To The Quiz.")

#This Is The Set Of Question Being Asked
#Question 1

    print("\nQuestion: 1 | score: {}".format(score))
    ans=input("What country has the largst population?\na.China\nb.India\nc.Brazil\nd.United States of America\ne.Your Answer is: : ")
    if ans == 'China' or ans == 'china' or ans == 'A' or ans == 'a':
        print('Correct')
        score +=1
        correct +=1
        print("Your Score is", score)
    else:
        print('Incorrect, the correst answer was China')
        if score <=0:
            score =0
            incorrect +=1


#Question 2

    print("\nQuestion: 2 | score: {}".format(score))
    ans=input("What is the oldest country in the world?\na.Japan\nb.Austria\nc.San Marino\nd.China\ne.Your Answer is: : ")
    if ans == 'San Marino' or ans == 'san marino' or ans == 'San marino' or ans == 'C' or ans == 'c':
        print('Correct')
        score +=1
        correct +=1
        print("Your Score is", score)
    else:
        print('Incorrect, the correct answer was San Marino')
        if score <=0:
            score =0
            incorrect +=1


#Question 3

    print("\nQuestion: 3 | score: {}".format(score))
    ans=input("What is the largest animal in the world?\na.Blue Whale\nb.African Elephant\nc.Colossal Squid\nd.Giraffe\ne.Your Answer is: : ")
    if ans == 'Blue Whale' or ans == 'blue whale' or ans == 'Blue whale' or ans == 'A' or ans == 'a':
        print('Correct')
        score +=1
        correct +=1
        print("Your Score is", score)
    else:
        print('Incorrect, the largest animal in the world is blue whale')
        if score <=0:
            score =0
            incorrect +=1


#Question 4

    print("\nQuestion: 4 | score: {}".format(score))
    ans=input("What is the longest river in the world?\na.Amazon river\nb.Yellow river\nc.Nile river\nd.Yangtze river\ne.Your Answer is: : ")
    if ans == 'Nile river' or ans == 'nile river' or ans == 'C' or ans == 'c':
        print('Correct')
        score +=1
        correct +=1
        print("Your Score is", score)
    else:
        print('Incorrect, the longest river in the world is the Nile river')
        if score <=0:
            score =0
            incorrect +=1



#Question 5

    print("\nQuestion: 5 | score: {}".format(score))
    ans=input("In what city would you find the red square?\na.Tokyo\nb.Budapest\nc.Vienna\nd.Moscow\ne.Your Answer is: : ")
    if ans == 'Moscow' or ans == 'moscow' or ans == 'D' or ans == 'd':
        print('Correct')
        score +=1
        correct +=1
        print("Your Score is", score)
    else:
        print('Incorrect, the city you would find the red square in would be Moscow')
        if score <=0:
            score =0
            incorrect +=1


            

#Question 6

    print("\nQuestion: 6 | score: {}".format(score))
    ans=input("In what century was the Mona Lisa painted?\na.16th\nb.13th\nc.17th\nd.14th\ne.Your Answer is: : ")
    if ans == '16th' or ans == '16' or ans == 'A' or ans == 'a':
        print('Correct')
        score +=1
        correct +=1
        print("Your Score is", score)
    else:
        print('Incorrect, the century the Mona Lisa was painted in was the 16th century')
        if score <=0:
            score =0
            incorrect +=1



#Question 7

    print("\nQuestion: 7 | score: {}".format(score))
    ans=input("How many stripes are there on the USA flag?\na.11\nb.13\nc.15\nd.18\ne.Your Answer is: : ")
    if ans == '13' or ans == 'thirteen' or ans == 'B' or ans == 'b':
        print('Correct')
        score +=1
        correct +=1
        print("Your Score is", score)
    else:
        print('Incorrect, the amount of stripes on the USA flag is 13')
        if score <=0:
            score =0
            incorrect +=1



#Question 8

    print("\nQuestion: 8 | score: {}".format(score))
    ans=input("What country has the most islands in the world?\na.New Zealand\nb.Canada\nc.Norway\nd.Sweden\ne.Your Answer is: : ")
    if ans == 'Sweden' or ans == 'sweden' or ans == 'D' or ans == 'd':
        print('Correct')
        score +=1
        correct +=1
        print("Your Score is", score)
    else:
        print('Incorrect, the country with the most amount of islands is Sweden')
        if score <=0:
            score =0
            incorrect +=1

#Question 9

    print("\nQuestion: 9 | score: {}".format(score))
    ans=input("In football which football club has won the most Champions leagues (formerly the European Cup)?\na.Bayern Munich\nb.Manchester United\nc.Real Madrid\nd.Liverpool FC\ne.Your Answer is: : ")
    if ans == 'Real Madrid' or ans == 'Real madrid' or ans == 'real madrid' or ans == 'C' or ans == 'c':
        print('Correct')
        score +=1
        correct +=1
        print("Your Score is", score)
    else:
        print('Incorrect, the football club with the most Champions leagues is Real Madrid CF')
        if score <=0:
            score =0
            incorrect +=1



#Question 10

    print("\nQuestion: 10 | score: {}".format(score))
    ans=input("What country in the world has the longest coastline?\na.Russia\nb.Canada\nc.Norway\nd.Indonesia\ne.Your Answer is: : ")
    if ans == 'Canada' or ans == 'canda' or ans == 'B' or ans == 'b':
        print('Correct')
        score +=1
        correct +=1
        print("Your Score is", score)
    else:
        print('Incorrect, the country with the longest coastline is Canada')
        if score <=0:
            score =0
            incorrect +=1



    print("You got", correct, "questions correct")
    print("You got", incorrect,"Questions incorrect")
    print("Thank you for playinig this general knowledge quiz")

