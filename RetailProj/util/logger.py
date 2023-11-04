import logging
# get a logger object
logger=logging.getLogger()
# create a logger handler to define where to output the log
# logging.StreamHandler: is to output the log into control pannel
stream_handler=logging.StreamHandler()
# logging.FileHandler: is to output the log into a file
file_handler=logging.FileHandler(
    filename='../log/test.log',
    mode='w',
    encoding='UTF-8'
)

# set a formatter object
fmt=logging.Formatter(
    "%(asctime)s - [%(levelname)s]  - %(filename)s - [%(lineno)d] : %(message)s"
)
stream_handler.setFormatter(fmt)
# add this logging handler to the logger object
logger.addHandler(stream_handler)
logger.addHandler(file_handler)
# set a logging level, the default logging level is 30: warning
logger.setLevel(10)
logger.debug('this is a debug log')
logger.info("this is info log") #it's not excuted
logger.warning('this is a warning')
logger.error('this is a error')
logger.critical('this is a critical log')

