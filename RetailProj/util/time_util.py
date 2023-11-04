import time
def ts10_to_date_str(ts,format="%Y-%m-%d %H:%M:%S"):
    time_array=time.localtime(ts)
    time.strftime(format,time_array)
def ts13_to_date_str(ts,format="%Y-%m-%d %H:%M:%S"):
    ts=int(ts/1000)
    ts10_to_date_str(ts)
