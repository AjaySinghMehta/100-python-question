''' angle between hour hand and minute hand of the clock
    suppose clock shows 9:00 then the angle is 90 degrees
    we will take the time as input hour and min separately

    basic info = each hour hand represents 30 degrees in a clock
                 and with each passig minute hour hand moves 0.5 degrees with minute hand
                => hour angle = 30*hour + 0.5*minute
        
               2- each minute hand represents 6 degrees in a clock     
                => minute angle = 6*minute
            
'''

def angle(hour, minute):
    hourAngle = 30*hour + 0.5*minute
    minAngle = 6*minute
    result = abs(hourAngle - minAngle)
    result = min(result, 360-result)
    return result

hour = int(input('enter hour : '))
minute = int(input('enter minute : '))
if (hour < 0 or minute < 0 or hour>12 or minute > 60):
    print('invalid input')
else:
    print(f' the angle between hour and minute hand at {hour}:{minute} is {angle(hour, minute)} degrees')
    
