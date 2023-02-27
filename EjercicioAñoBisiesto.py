
def is_year_leap(year):
    if ((year%400 == 0) or (year%100!=0) and (year&4 == 0)):
        print("it's a leap year")
    else:
        print("it's not a leap year")
    
year=int(input("Enter a year:- "))
is_year_leap(year)

