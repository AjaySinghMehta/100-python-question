# leap year = a year with 366 days where feburary has 29 days (example : 2024)

def leapYear(year):
    if year%4!=0:
        print(f'the year {year} is not a leap year')
    else:
        print(f'the year {year} is a leap year')

year = int(input('enter the year :'))

leapYear(year)

