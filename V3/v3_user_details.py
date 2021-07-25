#this is a simple program based on asking user for their details 
#initial score


score = 0
#ask for name
def greet():
    global name
    while True:
        name = input("Please enter your name : ")
        if name.replace(' ','').isalpha():
            break
        print("Please only use letters to enter your name.")
greet()

#ask for age
while True:
    age = input("Please enter your age : ")
    if age.replace(' ','').isnumeric():
        break
    print("Please only use numbers to enter your name.")
