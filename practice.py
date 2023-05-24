# def is a key word used to create functions in python

def new_function():
    print('Hey am a new function')

new_function()

#scope is the region where a variable has been created
# concatination is joining two variables to create a single ouput

def full_name(first_name, second_name):
    print (first_name + " " + second_name)

full_name("Abdihakim", "Mohamed")

pass_mark = 60

def student_grade(marks):
    if marks < pass_mark:
        print("student has failed")

    else:
        print("student has passed")

student_grade(10)