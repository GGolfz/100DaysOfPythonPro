height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round(weight/(height*height))
type = ''
if bmi <= 18.5:
    type = 'underweight'
elif bmi <= 25:
    type = 'normal weight'
elif bmi <= 30:
    type = 'overweight'
elif bmi <= 35:
    type = 'obese'
else:
    type = 'clinically obese'
print("Your BMI is "+str(bmi)+", you are "+str(type)+".")