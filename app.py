import datetime

today = datetime.date.today()

current_year = datetime.date.today().year

year = int(input('Year: '))
month = int(input("Month: "))
day = int(input("Day: "))
name = str(input("Name: "))

birthdate = current_year - year

birthday = datetime.date(year, month, day)

days_since_birth = (today - birthday).days

print(name, "has have lived for", days_since_birth, "days on earth and is currently", birthdate, "Years old.")