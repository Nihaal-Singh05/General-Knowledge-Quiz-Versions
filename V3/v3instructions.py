#This program is to ask the user if they want instructions for their quiz
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
       
