#BMI (Body Mass Index) project
#Code Author: Sabit

#input values-
weight = (float(input("Body weight (Kg): ")))
feet = (int(input("Height (feet): ")))
inch = (int(input("Height (inch): ")))

#convert feet and inch to metre-
height = ((feet*12 + inch)*2.54)/100

# BMI calculations
bmi = weight/(height ** 2)
print("Your BMI is:" , bmi)

#Our Body conditions-
if bmi>25 and bmi<29:
  print("Your weight is high.")
elif bmi>10 and bmi<25:
  print("Your weight is very low.")
elif bmi>29 and bmi<35:
  print("Your weight is high and fat body")
elif bmi>35 and bmi<40:
  print("You will die soon :(")
