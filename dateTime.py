import  datetime as dt
now = dt.datetime.now()

statement = f"{now.year}, {now.month}, {now.day}, {now.hour}, {now.minute}, {now.second}"

print(statement)

my_date = dt.datetime(year=1997 , month= 2 , day= 5, hour=20, minute=38, second=32)
print(my_date)