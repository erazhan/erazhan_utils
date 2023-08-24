# 版本更新需要保证代码兼容(原使用代码不出问题)
__version__ = "0.0.8"

from . import time_utils,json_utils,logging_utils
from . import os_utils,special_utils,sklearn_utils
from . import trie_tree

# 常用的一些函数，尽量保持不轻易变化
from .time_utils import get_time, get_today, backto_Ndays, backto_Ntoday
from .json_utils import read_json_file, save_json_file, read_txt_file, save_txt_file, trans2json
from .logging_utils import create_log_file, FileLogger, write_logger, update_logger
from .special_utils import remove_emoji,remove_quote,trans_singleQM2doubleQM,sort_dict, judge_not
#  from .conn_pg import MysqlConnection