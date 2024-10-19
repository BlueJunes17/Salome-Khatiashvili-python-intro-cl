from datetime import datetime

input_date = input("Please enter date YYYY-MM-DDThh:mm:ss.ms+hh:mm : ")

right_date = datetime.fromisoformat(input_date)


year = right_date.year
month = right_date.month
day = right_date.day
hour = right_date.hour 
minute = right_date.minute
second = right_date.second
timezone = right_date.tzinfo

#თაიმზონის განსაზღვრა :')
if right_date.tzinfo:
    timezone_offset = right_date.tzinfo.utcoffset(None).total_seconds() // 3600
    sign = '+' if timezone_offset >= 0 else '-'
    timezone = f"{sign}{abs(int(timezone_offset))}"   #abs გვაძლევს არაუარყოფით რიცვხებს
else:
    timezone = "+0"

# დეითების დაფორმატირება
new_date = f"{day:02d}-{month:02d}-{year} {hour}:{minute:02d}:{second:02d} {timezone}"

print(new_date)
