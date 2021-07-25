#this program is for scoring mechanics on version 2 
#question 1

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

#question 2 

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
