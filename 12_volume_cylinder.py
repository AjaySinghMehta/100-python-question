# volume of a cylinder is pi*r*r*h     for this we need radius of the cylinder 
# 1 cubic cm = 0.001 litres
from math import pi
radius = float(input('enter the radius of cylinder : '))
height = float(input('enter the height of cylinder : '))

volume = round((pi*radius*radius*height),2)


print(f'volume of the cylinder with radius {radius}cm and height {height}cm is {volume}cubic cm')
print(f'\nthe cost of the milk presnt in the cylinder of volume {volume}cubic cm is ruppes {round(volume*0.001*40,2)}')