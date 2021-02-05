#!/usr/bin/env python
# coding=utf-8

import logging
import os

class Log:
    def __init__(self):
	# 日志部分
        self.log_name = "./clock.log"
        self.logger = logging.getLogger(self.log_name)
        self.logger.setLevel(logging.DEBUG)

        log_path = os.path.dirname(os.path.abspath(__file__))
        logname = log_path + '/' + 'clock.log'  # 指定输出的日志文件名

        fh = logging.FileHandler(logname, mode='a', encoding='utf-8')  
	# 不拆分日志文件，a指追加模式,w为覆盖模式
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-[日志信息]: %(message)s',
                                      datefmt='%a, %d %b %Y %H:%M:%S')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
    
    def info_log(self, msg):
        self.logger.info(msg)

    def info_err(self, msg):
        self.logger.error(msg)
