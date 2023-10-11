# -*- coding = utf-8 -*-
# @time: 2022/2/18 5:49 下午
# @Author: erazhan
# @File: time_utils.py

# ----------------------------------------------------------------------------------------------------------------------
import time

from .constants import SECONDS_PER_DAY


def backto_Ndays(N, data_format = '%Y-%m-%d'):
    """计算前N天的0点时刻, N=1计算的是当天"""
    cutoff_time=time.strftime(data_format, time.localtime(time.time()-86400*(N-1)))+" 00:00:00"
    return cutoff_time


def backto_Ntoday(N, data_format = '%Y%m%d'):
    """计算前N天的日期名称, N=1计算的是当天"""
    cutoff_time=time.strftime(data_format, time.localtime(time.time()-86400*(N-1)))
    return cutoff_time


def get_time():
    return time.strftime("%Y-%m-%d %H:%M:%S")


def get_today():
    return time.strftime("%Y%m%d")


def is_leap_year(year):
    """
    判断是否为闰年:
    能被4整除且不能被100整除；能被400整除
    """
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False


def get_month_day(year, month):
    """
    判断某年某月有几天
    """
    year = int(year)
    mon = int(month)
    assert mon >= 1 and mon <=12,"月份必须在1-12月"

    m_31 = [1,3,5,7,8,10,12]
    m_30 = [4,6,9,11]

    if mon == 2:
        if is_leap_year(year):
            return 29
        else:
            return 28
    if mon in m_30:
        return 30

    if mon in m_31:
        return 31


def trans_str2struct(str_time, date_format = "%Y-%m-%d %H:%M:%S"):
    """
    str转struct_time
    date_format = "%Y-%m-%d %H:%M:%S,%f
    struct_time中的tm_isdst表示是否为夏令时
    tm_isdst = -1表示不确定, = 0 代表不是, = 1代表是
    """
    return time.strptime(str_time, date_format)


def trans_struct2timestamp(struct_time):
    """struct_time转timestamp"""
    return time.mktime(struct_time)


def trans_timestamp2struct(timestamp):
    """timestamp转struct_time"""
    return time.localtime(timestamp)


def trans_struct2str(struct_time,data_format = "%Y-%m-%d %H:%M:%S"):
    """struct_time转str"""
    return time.strftime(data_format,struct_time)


def trans_timestamp2str(timestamp,data_format = "%Y-%m-%d %H:%M:%S"):
    """timestamp转str"""
    return trans_struct2str(trans_timestamp2struct(timestamp),data_format = data_format)


def calculate_day_interval(start_day, end_day, data_format="%Y-%m-%d"):
    """计算两个日期的间隔天数
    :param start_day: 起始日期，2022-01-01
    :param end_day: 结束日期，2023-01-01
    :param data_format: 日期格式，默认为"%Y-%m-%d"，需要根据日期的格式进行调整
    :return: 间隔天数
    """
    start_timestamp = trans_struct2timestamp(trans_str2struct(start_day, date_format=data_format))
    end_timestamp = trans_struct2timestamp(trans_str2struct(end_day, date_format=data_format))

    timestamp_interval = end_timestamp - start_timestamp

    day_interval = int(timestamp_interval / SECONDS_PER_DAY)

    return day_interval


def calculate_next_day(start_day, day_interval, data_format = "%Y-%m-%d"):
    """根据起始日期和间隔天数计算结束日期
    :param start_day: 起始日期
    :param day_interval: 间隔天数
    :param data_format: 日期格式
    :return: 结束日期
    """
    start_timestamp = trans_struct2timestamp(trans_str2struct(start_day, date_format=data_format))
    next_timestamp = start_timestamp + day_interval * SECONDS_PER_DAY
    next_day = trans_timestamp2str(next_timestamp, data_format=data_format)

    return next_day


def predict_next_day(number_1 = 3499, date_1 = "2019-03-14", number_2 = 6299, date_2 = "2021-08-20"):

    print("number_1", number_1)
    print("date_1", date_1)
    print("number_2", number_2)
    print("date_2", date_2)
    print("-"*100)

    last_day_interval = calculate_day_interval(date_1, date_2)
    print("last_day_interval:", last_day_interval)
    print("last_year_interval:", last_day_interval / 365)

    last_avg_daily = number_1 / last_day_interval
    print("last_avg_daily:", last_avg_daily)

    next_day_interval = int(number_2 / last_avg_daily)
    print("next_day_interval:", next_day_interval)
    print("next_year_interval:", next_day_interval / 365)

    next_day = calculate_next_day(date_2, next_day_interval)
    print("next_day:", next_day)


if __name__ == "__main__":
    predict_next_day()
    pass