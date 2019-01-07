import datetime
import calendar

def create_calendar_page(month = None, year = None):
    toDay = datetime.datetime.today()
    calendar_ptr = '--------------------\nMO TU WE TH FR SA SU\n--------------------\n'

    if month == None:
        month = toDay.month

    if year == None:
        year = toDay.year
    toDay = datetime.datetime(year, month, 1)

    if isinstance(year, int):
        if isinstance(month, int) and month > 0 and month < 13:
            flag = 0
            for i in range(toDay.isoweekday() - 1):
                calendar_ptr += '   '
                flag += 1
            
            for i in range(calendar.monthrange(toDay.year, toDay.month)[1]):
                flag += 1

                if i < 9 and flag != 7:                    
                    calendar_ptr += '0' + str(i+1) + ' '
                elif i < 9 and flag == 7:
                    calendar_ptr += '0' + str(i+1)
                elif i + 1 == calendar.monthrange(toDay.year, toDay.month)[1]:
                    calendar_ptr += str(i+1)
                elif flag == 7:
                    calendar_ptr += str(i+1)
                else:
                    calendar_ptr += str(i+1) + ' '
                
                if flag == 7 and i != calendar.monthrange(toDay.year, toDay.month)[1]:
                    flag = 0
                    calendar_ptr += '\n'
        
            return (calendar_ptr)

print (create_calendar_page(1))
print (create_calendar_page())
print (create_calendar_page(3))
print (create_calendar_page(4, 1992))
print (create_calendar_page(12, 2019))