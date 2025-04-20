# BMI CALCULATOR
height = float(input("Enter your height  : ")) #in meters
weight = float(input("Enter your weight : "))  #in kg
bmi = weight / (height ** 2)                   #bmi formula
print("Your BMI is:", round(bmi, 2))           #round is used to round the value to two decimal places.
if bmi >= 30:
    print("Category: Obesity")
elif bmi >= 25:
    print("Category: Overweight")
elif bmi >= 18.5:
    print("Category: Normal")
else:
    print("Category: Underweight")

    #-----------------------output-----------------------
   # Enter your height  : 1.5
    #Enter your weight : 46
    # Your BMI is: 20.44
    #Category: Normal
