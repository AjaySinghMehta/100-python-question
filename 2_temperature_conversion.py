# Fahrenheit = (celsisu * 9/5) + 32
# using the above formula we will be doing this

unit = input("enter the unit of temperature as 'c' for celsius and 'f' for Fahrenheit': ")

def solution(unit):
    if unit[0]=='c':
        temp = float(input('enter the temperature in celsius: '))
        temp2 = (temp*9/5)+32
        print(f'The temperature {temp} celsius is equals to {temp2} fahrenheit')
    else:
        temp = float(input('enter the temperature in fahrenheit: '))
        temp2 = (temp-32)*5/9
        print(f'The temperature {temp} fahrenheit is equals to {temp2} celsius')
    
solution(unit)