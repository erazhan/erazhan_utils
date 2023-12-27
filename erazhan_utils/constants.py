# coding:utf-8
# -*- coding:utf-8 -*-
# @time: 2023/9/20 17:15
# @Author: erazhan
# @File: constants.py

# ----------------------------------------------------------------------------------------------------------------------
import string

# 后缀类型字典
SUFFIX_TYPE_DICT = {"图片":[".jpg",".jpeg",".png",".bmp" ,".webp"],
                    "PDF":[".pdf"],
                    "语音":[".wav",".mp3",".mp3}"],
                    "视频":[".mp4",".mp4}"]}

EN_PUNCTUATION = string.punctuation
CN_PUNCTUATION = "，。、：；？！“”（）《》【】「」"
ALL_PUNCTUATION = EN_PUNCTUATION + CN_PUNCTUATION
FULL_ANGLE_DIGITS = "０１２３４５６７８９"

SECONDS_PER_DAY = 86400