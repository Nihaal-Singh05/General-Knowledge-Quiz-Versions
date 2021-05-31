#this_program_asks_user_if_they_are_ready_to_begin_my_quiz

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
