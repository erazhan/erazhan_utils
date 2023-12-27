# 版本更新需要保证代码兼容(原使用代码不出问题)
__version__ = "0.0.13"

from . import time_utils,json_utils,logging_utils
from . import os_utils,special_utils
# from . import sklearn_utils
from . import trie_tree

# 常用的一些函数，尽量保持不轻易变化
from .time_utils import get_time, get_today, backto_Ndays, backto_Ntoday, calculate_day_interval, calculate_next_day
from .json_utils import read_json_file, save_json_file, read_txt_file, save_txt_file, trans2json
from .logging_utils import create_log_file, FileLogger, write_logger, update_logger
from .special_utils import remove_emoji, remove_quote, trans_singleQM2doubleQM, sort_dict, drop_same_words, split_text_by_puncation
from .judge_utils import judge_not, judge_negative_entity, judge_suffix,split_name_and_suffix, judge_suffix_type, split_hit_prefix_or_suffix
from .re_utils import clean_illegal_character, extract_text_between_strings, extract_text_after_string
from .math_utils import radian2angle, angle2radian, calculate_polygon_area, is_point_in_polygon

from .constants import SUFFIX_TYPE_DICT, EN_PUNCTUATION, CN_PUNCTUATION, ALL_PUNCTUATION, SECONDS_PER_DAY, FULL_ANGLE_DIGITS
#  from .conn_pg import MysqlConnection