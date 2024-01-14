# -*- coding: utf-8 -*-
"""BMI Calculator.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1o1FBvB1mDqRiZrwZ2B8huQpr1wclOmxx
"""

weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

height_in_meters = height / 100
BMI = weight/ (height_in_meters**2)
print(BMI)

if (BMI < 16):
  print ("You are severely underweight"), BMI

elif (BMI>= 16 and BMI < 18.5):
   print ("You are Underweight"), BMI

elif (BMI>= 18.5 and BMI < 24):
  print ("You are Healthy"), BMI

elif (BMI >= 25 and BMI < 30):
  print ("You are Overweight"), BMI

elif (BMI >=30):
  print ("You are Obese"), BMI