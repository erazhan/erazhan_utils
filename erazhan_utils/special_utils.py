# -*- coding = utf-8 -*-
# @time: 2022/2/23 3:01 下午
# @Author: erazhan
# @File: special_utils.py

# ----------------------------------------------------------------------------------------------------------------------
# 本文件设置一些其它的一些特殊通用

import time
from datetime import datetime
import re

def get_expire_date(N = 1, mode = "static", hour = 1):

    '''
    :param N: default = 1, N = 1, 接下去的第N天
    :param mode: defalut = "static": 固定在第N天的凌晨1点, "dynamic": 在当前时刻(精确到秒)后第N天的同一时刻
    :return:
    '''

    TN = time.localtime(time.time() + 86400 * N)

    # next_day
    year = TN.tm_year
    month = TN.tm_mon
    day = TN.tm_mday

    if mode == "static":
        # 设置为凌晨1点
        hour = hour
        minute = 0
        second = 0
    elif mode == "dynamic":
        # 第N天的同一时刻
        hour = TN.tm_hour
        minute = TN.tm_min
        second = TN.tm_sec
    else:
        raise ValueError("mode error: %s"%mode)

    dt = datetime(year, month, day, hour, minute, second)

    return dt

def remove_emoji(record):

    # content = "BGM好好听[失望][失望][失望][皱眉][皱眉]"

    # content = "chat:[破涕為笑]以前有过 chat:[微笑][握手] chat:[微笑][握手][握手] chat:[强]您的健康意识还是不错的"
    pattern = re.compile(r'\[.\]|\[..\]|\[...\]|\[....\]|\[.....\]|\[......\]')

    # emojis = pattern.findall(record) # 抽取表情包
    try:
        text = pattern.sub("", record) # 去除表情包
    except:
        text = record

    if len(text):
        return text
    else:
        return "空"

def remove_quote(record):

    record = "".join(record.strip().split())
    # quote = "- - - - - - - - - - - - - - -"
    quote = "---------------"
    if quote not in record:
        return record
    try:
        new_record = record.split(quote)[-1]
    except:
        new_record = record

    if len(new_record):
        return new_record
    else:
        return "空"

def trans_singleQM2doubleQM(text):
    '''将文本中的单引号转为双引号，便于后续使用json.loads
    QM: quotation marks
    '''
    try:
        text = re.sub('\'', '\"', text)
    except:
        pass

    return text

def sort_dict(raw_dict, sort_index = 1):

    new_dict = dict(sorted(list(raw_dict.items()),key = lambda x:x[sort_index],reverse= True))

    return new_dict

def padding_zero(num, digit=0):

    assert type(num)==int and num>=0
    str_num = str(num)
    if digit < len(str_num):
        digit = len(str_num)
    if len(str_num)<digit:
        str_num = "0" * (digit-len(str_num)) + str_num

    return str_num

def drop_same_words(old_list):
    """去除重复元素，并且保持原来的顺序"""
    new_list = []

    for one_kw in old_list:
        one_kw = one_kw.strip()

        if one_kw not in new_list:
            new_list.append(one_kw)

    return new_list

def split_text_by_puncation(text, punctuation = "。，,?？!！；：;:"):
    """按标点符号拆分句子"""
    try:
        split_pre_texts = re.split(r"[%s]"%punctuation,text)
    except:
        split_pre_texts = [text]

    return split_pre_texts

if __name__ == "__main__":

    text = "霓虹，测试;标点,符号。"
    result = split_text_by_puncation(text)
    print(result)
