"""
This is a code ues a function to calculates weeks remaining according to a life expectancy article written
By Tim Urban in 2014 https://waitbutwhy.com/2014/05/life-weeks.html  . 
"""

#Life Expectancy in weeks

def life_in_weeks(age):
    total_years = 90
    yearly_weeks = 52
    weeks_left = (total_years * yearly_weeks) - ( age * yearly_weeks )
    print(f"You have {weeks_left} weeks left.")
    
    
    
life_in_weeks(56)