# pylint: disable=C0114, C0115, C0116, C0103
name = input("What is your name? ")
year_born = (int(input("What year were you born? ")))
current_year = 2025
age = str(current_year - year_born)
weight = float(input("What is your weight in pounds? "))
height = float(input("What is your height in inches? "))
bmi = round(weight / (height * height) * 703, 2)
print("Hello " + name + "! You are " + age +
      " years old and your BMI is " + str(bmi) + ".")
if bmi < 18.5:
    print("You are underweight by " + str(round(18.5 - bmi, 2)) + "lbs")
elif bmi > 25:
    print("You are overweight by " + str(round(bmi - 25, 2)) + "lbs")
else:
    print("You are at a healthy weight.")
weight_range = input("do you want to know your ideal weight? ")
if weight_range == "yes":
    ideal_weight = str(round(24.9 * (height * height) / 703, 1))
    print("You should be at " + ideal_weight + " pounds.")
