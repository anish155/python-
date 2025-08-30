import calendar
import datetime

today=datetime.date.today()
yy=today.year
mm=today.month
day=today.day

cal = calendar.monthcalendar(yy, mm)

print(calendar.month_name[mm], yy)
print("Mo Tu We Th Fr Sa Su")

for week in cal:
    line = ""
    for d in week:
        if d == 0:  
            line += "   "
        elif d == day:
            
            line += f"[{str(d).rjust(2)}]"
        else:
            line += f" {str(d).rjust(2)} "
    print(line)
