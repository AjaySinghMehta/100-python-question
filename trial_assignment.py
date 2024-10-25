'''
monster game:
You have a list of points you get after defeating monsters.
If you defeat a monster in an even position (like the 2nd, 4th, etc.), the points from that monster are doubled.
You can choose to skip certain monsters to get the highest possible score.
The goal is to calculate the maximum possible score by deciding which monsters to defeat and which to skip.

ex 1:

arr = [2,3,4,5,1]
output = 
2 + 2*3 + 4 + 2*5 + 1 = 23

ex 2. 

arr = [2,1,3,5,1,1,7]
output = 
2+2*1+3+2*5+1+2*7 = 32
skipped 5th element i.e. 1 to gain twice the amount of 7
'''
