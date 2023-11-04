# grade of logging from low to high:
# 1. debug
# 2.info
# 3.warning
# 4.error
# 5.critical
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format=f' file name:  %(filename)s, line No: %(lineno)d, time-stamp: %(asctime)s, message: %(message)s, logging leve: %(levelname)s',
    filename='log.txt',
    filemode='w'
)
logging.debug('... debuging')
logging.info('...this is logging info')
logging.warning('... this is warning')
logging.error('...this is error')
logging.critical('...this is critical')

