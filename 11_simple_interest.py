# simple interest = (principle*rate_of_interest*time)/100
principle = float(input('enter the principle amount: '))
roi = float(input('enter the rate of interest : '))
time = float(input('enter the time period (in years) : '))

print(f'The Simple interst on {principle} at rate of interest of{roi} kept for {time} years is {(principle*roi*time)/100}')