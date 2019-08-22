import logging
from logging import handlers

class Log:
    level_relations = {
        'debug':logging.DEBUG,
        'info':logging.INFO,
        'warning':logging.WARNING,
        'error':logging.ERROR,
        'crit':logging.CRITICAL
    }#日志级别关系映射
    
    # when=D，新生成的文件名上会带上时间
    def __init__(self,filename='logs\\test.log',level='info',when='D',backCount=3,fmt='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)#设置日志格式
        self.logger.setLevel(self.level_relations.get(level))#设置日志级别
        sh = logging.StreamHandler()#往屏幕上输出
        sh.setFormatter(format_str) #设置屏幕上显示的格式
        #  logging.handlers.RotatingFileHandler -> 按照大小自动分割日志文件，一旦达到指定的大小重新生成文件
        #  logging.handlers.TimedRotatingFileHandler  -> 按照时间自动分割日志文件 
        th = handlers.TimedRotatingFileHandler(filename=filename,when=when,backupCount=backCount,encoding='utf-8')#往文件里写入#指定间隔时间自动生成文件的处理器
        #实例化TimedRotatingFileHandler
        #interval是时间间隔，backupCount是备份文件的个数，如果超过这个个数，就会自动删除，when是间隔的时间单位，单位有以下几种：
        # S 秒
        # M 分
        # H 小时、
        # D 天、
        # W 每星期（interval==0时代表星期一）
        # midnight 每天凌晨
        th.setFormatter(format_str)#设置文件里写入的格式
        self.logger.addHandler(sh) #把对象加到logger里
        self.logger.addHandler(th)
        # if __name__ == '__main__':
        #     log = Logger('all.log',level='debug')
        #     log.logger.debug('debug')
        #     log.logger.info('info')
        #     log.logger.warning('警告')
        #     log.logger.error('报错')
        #     log.logger.critical('严重')
        #     Logger('error.log', level='error').logger.error('error')

    def error(self,content):
        self.logger.error(content)
    def critical(self,content):
        self.logger.critical(content)
    def warning(self,content):
        self.logger.warning(content)
    def info(self,content):
        self.logger.info(content)
    # def debug(self,content):
    #     self.logger.debug(content)

# 日志级别： debug < info < warning < error < critical
# logging.debug('debug级别，最低级别，一般开发人员用来打印一些调试信息')
# logging.info('info级别，正常输出信息，一般用来打印一些正常的操作')
# logging.warning('waring级别，一般用来打印警信息')
# logging.error('error级别，一般用来打印一些错误信息')
# logging.critical('critical 级别，一般用来打印一些致命的错误信息,等级最高')

# log=Log()
# log.error('hahhahaha')




# #创建一个logger
# logger=logging.getLogger()
# logger.setLevel(logging.INFO)

# #创建一个handler，将log写入文件
# fh=logging.FileHandler(log_path,mode='w',encoding='utf-8')
# fh.setLevel(logging.INFO)

# #再创建一个handler，将log输出到控制台
# ch=logging.StreamHandler()
# ch.setLevel(logging.INFO)

# #设置输出格式
# log_format="%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s"
# formatter=logging.Formatter(log_format)
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)

# #把handler添加到logger里
# logger.addHandler(fh)
# logger.addHandler(ch)

# logger.error(content)

