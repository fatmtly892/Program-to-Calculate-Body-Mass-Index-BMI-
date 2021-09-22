#!/usr/bin/env python
# coding: utf-8

# In[10]:


#Taking weight in kilograms and height in meters.
weight = float(input("please enter your weight in kilograms "))
height = float(input("please enter your height in meters "))
BMI = weight /(height**2)


# In[11]:


# Conditions to find out BMI category
if BMI <= 18.5:
    print("Your BMI is", BMI,"You are underweight")
elif (BMI>= 18.5 and BMI < 24.9):
    print("Your BMI is",BMI,"You are healthy")
 
elif ( BMI >= 24.9 and BMI < 30):
    print( "Your BMI is",BMI," You are overweight")
 
elif ( BMI >=30):
    print("Your BMI is" ,BMI,"You are Suffering from Obesity")
    

