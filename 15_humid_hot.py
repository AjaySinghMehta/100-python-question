# easy question displays the weather condition using if elif else
def weather(temp, humidity):
    if (temp>=30 and humidity>=90):
        print('The weather is Hot and Humid')
    elif (temp>=30 and humidity<90):
        print('The weather is Hot')
    elif (temp<30 and humidity>=90):
        print('The weather is Cool and Humid')
    else:
        print('The weather is Cool')
    
temp = float(input('enter the temperature : '))
humidity = float(input('enter the humidity : '))

weather(temp, humidity)