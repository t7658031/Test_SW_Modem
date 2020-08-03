import os
import time
from datetime import datetime



def get_local_time_info(val):
    time_ticket = time.strftime('%Y-%m-%d_%H:%M:%S', val)
    return time_ticket


# def get_local_time_info_milliseconds():
#    val = '2016-02-25 20:21:04.242'
#    time_ticket = time.strptime(val, '%Y-%m-%d %H:%M:%S.%f')
#    return time_ticket


if __name__ == "__main__":
    k = [1, 2, 3]
    print(len(k))
    for i in range(len(k)):
        k[i]
        print(k[i])
    print(os.cpu_count())
    print(os.getcwd())
    val1 = time.localtime()
    print(get_local_time_info(val1))
    # print(get_local_time_info_milliseconds())
    t = int(round(time.time() * 1000))
    print(time.time())
    print(t)
    r = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(t / 1000))
    print(type(r))
    #m = time.strftime('%Y-%m-%d %H:%M:%S.%f',)
    print(datetime.utcnow())
    print(datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3])
    print(time.localtime(t/1000000))

    date_time = datetime.now()
    print(date_time)
    print(date_time.timetuple())
    ans_time = time.mktime(date_time.timetuple())
    print(ans_time)

    print(r)
    a = 'log.txt'
    print(str(a)[:-4])
    #print(m)
