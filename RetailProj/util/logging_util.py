'''
1. import logging
2. define Logging class
    define a logger object as the attribute: logger by using getLogger
    set a log level
3. define a logger initialization funtion
    create a Logging instant: logger
    create a file / stream handler for where to output the log
    define log format by create a obj of formatter
    set handler's format
    assign the hander to the log instant
'''
import logging
from RetailProj.config import proj_config as config


class Logging:
    def __init__(self,level=20):
        self.logger=logging.getLogger()
        self.logger.setLevel(level)
def init_logger():
    logger=Logging().logger
    # judge if a logger already has a handler to exempt the cache avoiding duplicate logs
    if logger.handlers:
        return logger
    file_handler=logging.FileHandler(
        filename=config.log_root_path+config.log_name,
        mode='a',
        encoding='UTF-8'
    )
    fmt=logging.Formatter(
        "%(asctime)s - [%(levelname)s]  - %(filename)s - [%(lineno)d] : %(message)s"
    )
    file_handler.setFormatter(fmt)
    logger.addHandler(file_handler)
    return logger
if __name__ == '__main__':
    logger= init_logger()
    logger.info('this is a info')
    logger.warning('this is a warning')
    logger.error('this is an error')


    print(type(logger))



