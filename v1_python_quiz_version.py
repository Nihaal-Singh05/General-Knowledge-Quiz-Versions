#this_is_a_simple_quiz
#initial_score

score = 0

#ask_user_for_name
name = input("Enter Your Name : ")

#ask_user_for_age
age = int(input("Enter Your Age : "))

#ask_user_if_they_are_ready_to_take_the_quiz
status = input("Are you ready to take the genral knowledge quiz?\na. Yes \nb. No \n=>")

#what_if_user_is_not_ready
if status == 'No' or status == 'no' or status == 'B' or status == 'b' :
    print("See you soon.")
    exit()

#what_if_user_is_ready
if status == 'Yes' or status == 'yes' or status == 'A' or status == 'a' :
    print("Welcome to the General Knowledge quiz.")
    
#set_of_questions_that_are_asked
#question_1

print("\nQuestion: 1 | score: {}".format(score))
ans=input("What country has the largest population in the world?\na.India\nb.China\nc.America\nd.Your Answer is:  : ")
if ans == 'China' or ans == '' or ans == 'B' or ans == 'b':
    print('Well done, you are correct')
    score +=1
else:
    print('Incorrect')
    if score <=0:
        score =0

#question_2
print("\nQuestion: 2 | score: {}".format(score))
ans=input("In what city would you find the red square?\na.Vienna\nb.Tokyo\nc.Moscow\nd.Your Answer is:  : ")
if ans == 'Moscow' or ans == 'moscow' or ans == 'C' or ans == 'c':
    print('Well done, you are correct')
    score +=1
else:
    print('Incorrect')
    if score <=0:
        score =0

#question_3
print("\nQuestion: 3 | score: {}".format(score))
ans=input("What is the smallest country in the world?\na.Vatican City\nb.Monaco\nc.San Marino\nd.Your Answer is:  : ")
if ans == 'Vatican City' or ans == 'Vatican city' or ans == 'vatican city' or ans == 'A' or ans == 'a':
    print('Well done, you are correct')
    score +=1
else:
    print('Incorrect')
    if score <=0:
        score =0

#question_4
print("\nQuestion: 4 | score: {}".format(score))
ans=input("What is the biggest animal in the world?\na.Giraffe\nb.Elephant\nc.Blue Whale\nd.Your Answer is:  : ")
if ans == 'Blue Whale' or ans == 'Blue whale' or ans == 'blue whale' or ans == 'C' or ans == 'c':
    print('Well done, you are correct')
    score +=1
else:
    print('Incorrect')
    if score <=0:
        score =0

#question_5
print("\nQuestion: 5 | score: {}".format(score))
ans=input("What country in the world has the most islands?\na.Sweden\nb.Canada\nc.New Zealand\nd.Your Answer is:  : ")
if ans == 'Sweden' or ans == 'sweden' or ans == 'A' or ans == 'a':
    print('Well done, you are correct')
    score +=1
else:
    print('Incorrect')
    if score <=0:
        score =0

print("Thank You",name, "Aged", age, "for playing our quiz")
print("You score is", score)
       

