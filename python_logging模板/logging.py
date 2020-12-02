# encoding = utf-8
import sys,time
import os
import logging
import logging.handlers

class Log(object):
    def __init__(self, log_name):
        log_dir = 'logs'
        os.makedirs(log_dir, exist_ok=True)
        self._log_dir = log_dir
        self._log_name = log_name

    def set_logger(self):
        # 创建一个logger,可以考虑如何将它封装
        logger = logging.getLogger(self._log_name)
        logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件, 存 3 个日志，每个 10M 大小
        fh = logging.handlers.RotatingFileHandler(os.path.join(self._log_dir, self._log_name + '.log'),
                                                  maxBytes=10*1024*1024, backupCount=3)
        fh.setLevel(logging.DEBUG)
        # 再创建一个handler，用于输出到控制台
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s - %(module)s.%(funcName)s.%(lineno)d - '
                                      '%(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        # 给logger添加handler
        logger.addHandler(fh)
        logger.addHandler(ch)
        return logger

if __name__ == '__main__':
	time_begin = time.time()
	logger = Log(os.path.basename(__file__)).set_logger()
	result = ''
	try:
		# 调用方法 1
		# 调用方法 2
		result = '正常结果'
	except:
		# 记录控制台完整异常信息
		result = '异常结果'
		logger.exception(sys.exc_info())
	finally:
		# 返回或者记录结果
		logger.info(result)
		logger.info('共耗时 {0} 秒'.format(time.time() - time_begin))
