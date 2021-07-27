from datetime import date

birth_year = input('what is your birth year')

today = date.today()

year=today.year
print(year)
#print(type(birth_year))

print( f'your age is { year - int(birth_year)} ' )
