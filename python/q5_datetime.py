# Hint:  use Google to find python function

####a) 

from dateutil import parser

from datetime import datetime


date_start = '01-02-2013'  
date_stop = '07-28-2015'

date_start_object_1 = parser.parse(date_start)
date_stop_object_1 = parser.parse(date_stop) 
print (date_stop_object_1 - date_start_object_1)

####b)  
date_start = '12312013'  
date_stop = '05282015'


date_start_object_2 = datetime.strptime(date_start,'%m%d%Y')
date_stop_object_2 = datetime.strptime(date_stop,'%m%d%Y')
print (date_stop_object_2 - date_start_object_2)

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'  

date_start_object_3 = parser.parse(date_start)
date_stop_object_3 = parser.parse(date_stop) 
print (date_stop_object_3 - date_start_object_3)

