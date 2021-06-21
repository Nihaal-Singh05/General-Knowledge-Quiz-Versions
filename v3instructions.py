##Asking if user wants instructions
def inst():
    inst = input("If you wish to read the instructions for this quiz. (Enter Yes or No) :{}?: \na. Yes \nb. No \n=>")
    if inst == 'Yes' or inst == 'yes' or inst == 'Y' or inst == 'y' or inst == 'A' or inst == 'a':
     
        print("----------------------------------Instructions------------------------------------------") #instruction of the quiz 
        print("This quiz will ask questions based on general knowledge") 
        print("There will be four possible answers for every questions")
        print("However, there will only be one correct answer for each question.")
        print("----------------------------------------------------------------------------------------")
    else:
        print("Welcome to the General Knowledge quiz")
