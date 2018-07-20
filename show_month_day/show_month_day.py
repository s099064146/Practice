import sys
import time
import datetime

def year_month_date_list(year_s, month_s, date_s, year_e, month_e, date_e):
	
	try:
    StartDate = time.strptime(year_s+'/'+month_s+'/'+date_s, '%Y/%m/%d')
    EndDate = time.strptime(year_e+'/'+month_e+'/'+date_e, '%Y/%m/%d')
    StartDate = datetime.date(StartDate[0], StartDate[1], StartDate[2])
    EndDate =  datetime.date(EndDate[0], EndDate[1], EndDate[2])
    RangeDate = datetime.timedelta(days = 1)
    
    except ValueError :
    print('Please input interger in following region\n')
	print('Year: 1000~3000\n')
    print('Month: 1~12\n')
	print('Date: 1~31 (Month dependent)\n')
	
	#initialize list
    date_list =[]
    while StartDate <= EndDate:
        date_list.append(str(StartDate))
        StartDate = StartDate + RangeDate
		
    return date_list
	