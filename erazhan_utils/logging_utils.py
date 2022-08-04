# -*- coding = utf-8 -*-
# @time: 2022/2/21 11:22 上午
# @Author: erazhan
# @File: logging_utils.py

# ----------------------------------------------------------------------------------------------------------------------
import os
import time
import logging

def create_log_file(project_name = "emr",log_dir = "./app_logs", version = "test"):

    cur_time = time.strftime("%Y%m%d_%H%M%S")
    # mode='a'是会接在后面写的，mode='w'会覆盖掉之前日志
    app_log_name = "app_%s_%s_%s.log"%(project_name,version,cur_time)
    log_file = os.path.join(log_dir, app_log_name)
    return log_file

class FileLogger(object):

    '''
    使用方法：
    from utils import FileLogger

    # 需要区分
    test_FH = FileLogger("./logs")
    test_FH.create_logger(name = 'test')
    test_FH.logger.info("test logging")

    test_FH.create_logger(name = "new test")
    test_FH.logger.info("new test logging")
    '''

    def __init__(self, log_dir = "./app_logs/", update_type = "day"):

        if not os.path.exists(log_dir):
            os.mkdir(log_dir)

        self.log_dir = log_dir
        self.fh = None
        self.logger = None
        self.update_flag = True
        self.update_type = update_type

        self.last_mday = time.localtime().tm_mday
        self.last_min = time.localtime().tm_min
        self.last_sec = time.localtime().tm_sec

    # 创建logger
    def create_logger(self, log_file, logger_name = "disease", update_type = "day"):

        assert update_type == self.update_type, "update_type 不一致"
        TN = time.localtime()

        # 后续更新时间
        if update_type == "day":
            if TN.tm_mday != self.last_mday:
                self.update_flag = True
                self.last_mday = TN.tm_mday
        elif update_type == "min":
            if TN.tm_min != self.last_min:
               self.update_flag = True
               self.last_min = TN.tm_min
        elif update_type == "sec":
            if TN.tm_sec != self.last_sec:
                self.update_flag = True
                self.last_sec = TN.tm_sec
        else:
            raise ValueError("update_type %s error, require day or min or sec"%(update_type))

        if self.update_flag == False:
            return
        print("需要更新logger",log_file,self.update_flag,self.last_mday,TN.tm_mday,TN.tm_min,TN.tm_sec)
        # 没有
        self.update_flag = False
        if self.fh is not None:
            self.logger.removeHandler(self.fh)
            print("移除原来fh",log_file, self.update_flag, self.last_mday, TN.tm_mday,TN.tm_min,TN.tm_sec)

        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

        # 多种formatter形式
        self.formatter = []

        self.formatter.append(logging.Formatter("%(message)s"))
        self.formatter.append(logging.Formatter("[line:%(lineno)d] - %(levelname)s:\n %(message)s"))
        self.formatter.append(logging.Formatter("[line:%(lineno)d] %(asctime)s - %(levelname)s : %(message)s"))
        self.formatter.append(logging.Formatter("%(asctime)s - %(levelname)s : %(message)s"))
        self.formatter.append(logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'))

        self.fh = self.update_handler(self.formatter[4],log_file = log_file)

    # 每天凌晨更新日志文件
    def update_handler(self, formatter, log_file):

        new_fh = logging.FileHandler(log_file, mode='a')
        new_fh.setLevel(logging.INFO)
        new_fh.setFormatter(formatter)
        self.logger.addHandler(new_fh)

        return new_fh

def write_logger(text, the_FH, info_type = "info"):

    if info_type == "info":
        the_FH.logger.info(text)
    elif info_type == "error":
        the_FH.logger.error(text)
    else:
        pass

def update_logger(the_FH, project_name, app_log_dir, app_version_name, logger_name,update_type = 'day'):

    app_log_file = create_log_file(project_name, app_log_dir, version=app_version_name)
    the_FH.create_logger(app_log_file, logger_name = logger_name,update_type=update_type)

if __name__ == "__main__":

    app_log_dir = "./app_logs"
    project_name = "expert"
    logger_name = "inte_triage_expert_in" # 不重要
    update_type = "min"  # "day"
    app_version_name = "v1_offline"

    # emr_FH = FileLogger(log_dir = app_log_dir)
    # emr_FH.create_logger(log_file = app_log_file, logger_name = app_version_name) # 例如: logger_name = "v5_online"

    the_FH = FileLogger(log_dir=app_log_dir, update_type=update_type)
    app_log_file = create_log_file(project_name, app_log_dir, version=app_version_name)
    the_FH.create_logger(app_log_file, logger_name=logger_name, update_type=update_type)

    write_logger("创建初始日志,进程pid:%d" % os.getpid(), the_FH, info_type="info")

    for i in range(70):

        update_logger(the_FH, project_name, app_log_dir, app_version_name, logger_name, update_type=update_type)
        write_logger("count:%d" % (i + 1), the_FH, info_type='info')
        time.sleep(1)
