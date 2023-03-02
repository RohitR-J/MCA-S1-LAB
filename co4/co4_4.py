'''
Create a class Time with private attributes hour, minute and second. Overload ‘+’ operator to
find sum of 2 time.

'''

class Time:
    def __init__(self,hr,minu,sec):
    	self.__hr = hr
    	self.__minu = minu
    	self.__sec = sec
    	
    def gethr(self):
    	return self.__hr
    	
    def getminu(self):
    	return self.__minu
    	
    def getsec(self):
    	return self.__sec
    	
    def __add__(self,other):
    	hr = self.__hr + other.__hr
    	minu = self.__minu + other.__minu
    	sec = self.__sec + other.__sec
    	if sec >= 60:
    		minu += 1
    		sec -= 60
    	if minu>=60:
    		hr+=1
    		minu-=60
    	if hr>=24:
    		hr-=24
    
    	return Time(hr,minu,sec)
    	
time1 = Time(4,30,0)
time2 = Time(5,70,10)
total = time1+time2

print(total.gethr(),"|",total.getminu(),"|",total.getsec())

    	
    




