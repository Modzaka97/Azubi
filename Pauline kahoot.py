name = input("Enter your name: ")
age = input("Enter your age: ")
try:
    if int(age)>= 18:
        print("Hello " + name + ", you are eligible to continue the application for the job.")
    else:
        print("Sorry " + name + " , you are young and cannot apply for this job!")
except:
    print("Incorrect Input")
