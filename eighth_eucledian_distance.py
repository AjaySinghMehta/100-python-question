# eucledian distance is a distance between two points p(a,b) and q(x,y) 
# such that the distance d = sqrt((a-x)^2+(b-y)^2)

from math import sqrt,pow

#method 1: using 4 different variables

def eucledian_distance(x1,y1,x2,y2):
    distance = sqrt(pow((x1-x2),2) + pow((y1-y2),2))
    return distance
     
# method 2: using list
def eucledian(ls):
    x = ls[0]-ls[2]
    y = ls[1]-ls[3]
    distance = sqrt(pow(x,2) + pow(y,2))
    return distance



ls = []
for i in range(4):
    if i <= 1:
        z = 1
        if i%2 ==0:
            element = float(input(f'co-ordinate {z} x: '))
        else:
            element = float(input(f'co-ordinate {z} y: '))
            
    else:
        z = 2
        if i%2 ==0:
            element = float(input(f'co-ordinate {z} x: '))
        else:
            element = float(input(f'co-ordinate {z} y: '))

    ls.append(element)



# point1 = int(input('Enter the x co-ordinate of point 1 : '))
# point2 = int(input('Enter the y co-ordinate of point 1 : '))
# point3 = int(input('Enter the x co-ordinate of point 2 : '))
# point4 = int(input('Enter the y co_ordinate of point 2 : '))

# result = eucledian_distance(point1, point2, point3, point4)
result = eucledian(ls)

print(result)

