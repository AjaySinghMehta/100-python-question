'''
we are going to do 3 conversions 
1 -> centimeter to feet   1 cm = 0.0328084 foot
2 -> kilometer to miles   1 km = 0.62137119 mile
3 -> usd to inr           1 usd = 83.75 inr as i am writing this code
'''
from time import sleep

def conversion(u):
    if(u == 'c'):
        value = float(input('enter the value in centimeters : '))
        result = value*0.0328084
        print(f'{value} cm is equals to {result} foot')
    elif(u == 'k'):
        value = float(input('enter the value in kilometers : '))
        result = value*0.62137119
        print(f'{value} km is equals to {result} miles')
    elif(u == '$'):
        value = float(input('enter the amount in usd : '))
        result = value*83.75
        print(f'{value}$ is equals to INR {result}')
    else:
        print('not a valid input exiting...')
        sleep(2)
        
        
unit = input('enter unit (c -> centimeter, k -> kilometer, $ -> usd) : ').lower()
conversion(unit)
