#coding=utf-8
from datetime import datetime
import time

#把datetime转成字符串
def datetime_toString(dt,format="%Y-%m-%d-%H"):
    return dt.strftime(format)

#把字符串转成datetime
def string_toDatetime(string,format="%Y-%m-%d-%H"):
    return datetime.strptime(string, format)

#把字符串转成时间戳形式
def string_toTimestamp(strTime):
    return time.mktime(string_toDatetime(strTime).timetuple())

#把时间戳转成字符串形式
def timestamp_toString(stamp,format="%Y-%m-%d-%H"):
    return time.strftime(format, time.localtime(stamp))

#把datetime类型转成时间戳形式
def datetime_toTimestamp(dateTim):
    return time.mktime(dateTim.timetuple())

if __name__=="__main__":
    pass
    now=datetime.now()
    print(now)
    print(type(now))                    #<class 'datetime.datetime'>

    now_str=datetime_toString(now,format="%Y-%m-%d-%H")
    print(now_str,type(now_str))        #<class 'str'>

    timestamp =datetime_toTimestamp(now)
    print(timestamp, type(timestamp))  # <class 'float'>

    datetime_obj=string_toDatetime(now_str,format="%Y-%m-%d-%H")
    print(datetime_obj, type(datetime_obj))  # <class 'datetime.datetime'>

    timestamp=string_toTimestamp(now_str)
    print(timestamp,type(timestamp))        #<class 'float'>

    date_str=timestamp_toString(timestamp,format="%Y-%m-%d %H:%M")
    print(date_str,type(date_str))
