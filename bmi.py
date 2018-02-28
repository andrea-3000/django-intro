print("BMI Calculator")
age = int(input("How old are you? "))
weight = int(input("How much do you weigh in pounds? "))
height = int(input("How tall are you in inches? "))

bmi = weight/(height**2)*703

print("Your BMI is " + str(bmi))
