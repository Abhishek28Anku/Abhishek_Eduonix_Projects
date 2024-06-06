#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("*"*50)
print("Project: Survival Duration Program")
class AgeCalculator:
    def __init__(self, age):
        self.age= age
        print("you are", age, "years old")
        print("*"*50)
        self.choice()
    def choice(self):
        unit= input(""" Please choose your prefered time unit:
          1.Months,
          2.Weeks,
          3.Days,
          4.Hours,
          5.Minutes,
          6.Seconds
        Hint-Choose from the options mentioned above or enter the first letter of option
        """)
        if unit== "Months".lower() or unit== "M".lower():
            self.age_in_months()
        if unit== "Weeks".lower() or unit== "W".lower():
            self.age_in_weeks()
        if unit== "Days".lower() or unit== "D".lower():
            self.age_in_days()
        if unit== "Hours".lower() or unit== "H".lower():
            self.age_in_hours()
        if unit== "Minutes".lower() or unit== "M".lower():
            self.age_in_minutes()
        if unit== "Seconds".lower() or unit== "S".lower():
            self.age_in_seconds()

    def age_in_months(self):
        print("*"*50)
        print("Your Age In Months is: ",self.age* 12," Months")
        print("*"*50)

    def age_in_days(self):
        print("*"*50)
        print("Your Age In Days is: ",self.age* 365," Days.")
        print("*"*50)

    def age_in_weeks(self):
        print("*"*50)
        print("Your Age In Weeks is: ",self.age* 52.143, " Weeks.")
        print("*"*50)
    
    def age_in_hours(self):
        print("*"*50)
        print("Your Age In Hours is: ",self.age * 24 * 12,"Hours.")
        print("*"*50)

    def age_in_minutes(self):
        print("*"*50)
        print("Your Age In Minutes is: ",self.age* 24 * 12 * 60," Minutes.")
        print("*"*50)

    def age_in_seconds(self):
        print("*"*50)
        print("Your Age In Seconds is: ", self.age * 24 * 12* 60 * 60," Seconds.")
        print("*"*50)

    
# Example usage:
Age =AgeCalculator(20)



# 
