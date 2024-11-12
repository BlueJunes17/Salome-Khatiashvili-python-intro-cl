from datetime import datetime 

year = int(input(" დაბადების წელი: "))
month = int(input(" დაბადების თვე: "))
day = int(input(" დაბადების დღე: "))

week_day = datetime(year, month, day).strftime("%A")

print(week_day)