
import datetime

christmas= datetime.date(2023,12,25)
today=datetime.date.today()
days_till_christmas = christmas-today
print(days_till_christmas)

month = int(input('When is your birthday? [MM] '))
day = int(input('When is your birthday? [DD] '))
birthday = datetime.date(today.year,month,day)
if today> birthday:
    birthday= datetime.date(today.year+1,month,day)
days_till_birthday= birthday - today 
print(days_till_birthday)