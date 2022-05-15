#https://www.w3schools.com/python/gloss_python_date_format_codes.asp
#Date Format Codes
#A reference of all the legal format codes:
#該物件具有將日期物件格式化為可讀字串的方法。datetime
#Directive	Description	                Example	
#%a	        Weekday, short version	    Wed	
import datetime
x = datetime.datetime.now()
print(x.strftime("%a"))
print('-------------分隔線------------')
#%A	        Weekday, full version	    Wednesday	
import datetime
x = datetime.datetime.now()
print(x.strftime("%A"))
print('-------------分隔線------------')
#%w	        Weekday as a number 0-6,
#            0 is Sunday	            3	
import datetime
x = datetime.datetime.now()
print(x.strftime("%w"))
print('-------------分隔線------------')
#%d	        Day of month 01-31	        31	
import datetime
x = datetime.datetime.now()
print(x.strftime("%d"))
print('-------------分隔線------------')
#%b	        Month name, short version	Dec	
import datetime
x = datetime.datetime.now()
print(x.strftime("%b"))
print('-------------分隔線------------')
#%B	        Month name, full version	December	
import datetime
x = datetime.datetime.now()
print(x.strftime("%B"))
print('-------------分隔線------------')
#%m	        Month as a number 01-12	    12	
import datetime
x = datetime.datetime.now()
print(x.strftime("%m"))
print('-------------分隔線------------')
#%y	        Year, short version, 
#           without century	            18	
import datetime
x = datetime.datetime.now()
print(x.strftime("%y"))
print('-------------分隔線------------')
#%Y	        Year, full version	        2018	
import datetime
x = datetime.datetime.now()
print(x.strftime("%Y"))
print('-------------分隔線------------')
#%H	        Hour 00-23	                17	
import datetime
x = datetime.datetime.now()
print(x.strftime("%H"))
print('-------------分隔線------------')
#%I	        Hour 00-12	                05	
import datetime
x = datetime.datetime.now()
print(x.strftime("%I"))
print('-------------分隔線------------')
#%p	        AM/PM	                    PM	
import datetime
x = datetime.datetime.now()
print(x.strftime("%p"))
print('-------------分隔線------------')
#%M	        Minute 00-59	            41	
import datetime
x = datetime.datetime.now()
print(x.strftime("%M"))
print('-------------分隔線------------')
#%S	        Second 00-59	            08	
import datetime
x = datetime.datetime.now()
print(x.strftime("%S"))
print('-------------分隔線------------')
#%f	        Microsecond 000000-999999	548513	
import datetime
x = datetime.datetime.now()
print(x.strftime("%f"))
#%z	        UTC offset	                +0100	
#%Z	        Timezone	                CST	
print('-------------分隔線------------')
#%j	        Day number of year 001-366	365	
import datetime
x = datetime.datetime.now()
print(x.strftime("%j"))
print('-------------分隔線------------')
#%U	        Week number of year, Sunday as 
#           the first day of week, 
#           00-53                       52	
import datetime
x = datetime.datetime.now()
print(x.strftime("%U"))
print('-------------分隔線------------')
#%W	        Week number of year, Monday as 
#           the first day of week, 
#           00-53                       52	
import datetime
x = datetime.datetime(2018, 5, 31)
print(x.strftime("%W"))
print('-------------分隔線------------')
#%c	        Local version of date and 
#           time                        Mon Dec 31 17:41:00 2018	
import datetime
x = datetime.datetime.now()
print(x.strftime("%c"))
print('-------------分隔線------------')
#%x	        Local version of date	    12/31/18	
import datetime
x = datetime.datetime.now()
print(x.strftime("%x"))
print('-------------分隔線------------')
#%X	        Local version of time	    17:41:00
import datetime
x = datetime.datetime.now()
print(x.strftime("%X"))
print('-------------分隔線------------')
##%%	    A % character	            %
import datetime
x = datetime.datetime.now()
print(x.strftime("%%"))
#Related Pages 相關頁面
#Python DateTime Tutorial
#https://www.w3schools.com/python/python_datetime.asp
#Datetime Module 日期時間模組
#https://www.w3schools.com/python/gloss_python_date.asp
#Date Output 日期輸出
#https://www.w3schools.com/python/gloss_python_date_output.asp
#Create a Date Object 創建日期物件
#https://www.w3schools.com/python/gloss_python_date_create.asp
#The strftime Method 斯特夫時間方法
#https://www.w3schools.com/python/gloss_python_date_strftime.asp
#Date Format Codes 日期格式代碼
#https://www.w3schools.com/python/gloss_python_date_format_codes.asp
