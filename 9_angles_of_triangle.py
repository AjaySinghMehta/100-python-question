# easy sum of angles of triangle is always 180 no less no more

ls = []
for i in range(3):
    angle = float(input(f'angle {i+1} : '))
    ls.append(angle)

print(bool((ls[0]+ls[1]+ls[2]) == 180),'Triangle')
