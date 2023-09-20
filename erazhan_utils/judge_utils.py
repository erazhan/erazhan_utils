# coding:utf-8
# -*- coding:utf-8 -*-
# @time: 2023/8/30 17:54
# @Author: erazhan
# @File: judge_utils.py

# ----------------------------------------------------------------------------------------------------------------------
from .constants import SUFFIX_TYPE_DICT


def judge_not(entity, record):
    """保留原名称，兼容老版本"""
    return judge_negative_entity(entity, record)


def judge_negative_entity(entity, record):
    """判断entity和否定词的组合是否包含在原句子中，用于检查NER是否仅识别到不加否定前缀或后缀的entity。
    比如：entity='没有发烧'，NER如果仅识别到'发烧'，则可通过此函数粗略判断到识别内容不全，
    """
    neg_words = ["没有", "没", "无", "不", "不是"]
    re_neg_words = ["没有", "没", "无"]
    # 否定词在前
    flag = any(nw + entity in record for nw in neg_words)
    # 否定词在后
    re_flag = any(entity + rnw in record for rnw in re_neg_words)
    return flag or re_flag


def judge_suffix(text, suffix_list):
    """判断文本是否包含列表中的后缀，如果包含后缀返回纯的文件名和后缀名称"""
    return any(text.strip().endswith(suffix) for suffix in suffix_list)


def split_name_and_suffix(text, suffix_list):
    """将文本中的后缀名分离成名称+后缀，比如'123.jpg' -> '123'+'.jpg'"""
    text = text.strip()
    hit_name = None
    hit_suffix = None
    for suffix in suffix_list:
        if text.endswith(suffix):
            hit_name = text.split(suffix)[0]
            hit_suffix = suffix
            break
    return hit_name, hit_suffix


def judge_suffix_type(text, suffix_type_dict = SUFFIX_TYPE_DICT):
    """判断文本字符串的后缀类型，适用于多种后缀类型文件的判断，默认采用SUFFIX_TYPE_DICT"""
    text = text.strip()
    for suffix_type, suffix_list in suffix_type_dict.items():
        if judge_suffix(text,suffix_list):
            return suffix_type
    return "文字"


if __name__ == "__main__":

    text = "123.jpg"
    suffix_list = [".jpg",".png"]

    res = judge_suffix(text,suffix_list=suffix_list)
    print(res)

    hit_name, hit_suffix = split_name_and_suffix(text,suffix_list)
    print(hit_name)
    print(hit_suffix)

    text_type = judge_suffix_type(text)
    print(text_type)

    ent = "发烧"
    raw_text = "发烧的没有"
    a = judge_negative_entity(ent, raw_text)

    print(a)
    pass
