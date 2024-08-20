'''
CTC = cost to company
In hand salary = CTC - (HRA + DA + PF + Tax)
Tax = 5-10 lakh : 10% 
      10-20 lakh : 20%
      20lakh + : 30%
    
as you might already know for 5-10 lakh will always be 10*
and for 1 penny more than 10lakh i.e. for 12 lakh for first 10lakh 10% and for remaining 2 lakh 20%
that is the total tax payable
'''

def inHand(s):
    result = 0
    hra = (s*0.1)
    da = (s*0.05)
    pf =(s*0.03)
    tax = 0
    if(s<500000):
        tax = 0
    elif(s>=500000 and s<1000000):
        tax = s*0.1
    elif(s>=1000000 and s<2000000):
        tax = tax + 1000000*0.1 + (s-1000000)*0.2
    else:
        tax = tax + 1000000*0.1 + (s-1000000)*0.2 + (s-2000000)*0.3
    result = s - (hra + da + pf + tax)
    return result

salary = int(input('enter your salary : '))
inhand = inHand(salary)
print(f'Your Inhand salary is {inhand}')