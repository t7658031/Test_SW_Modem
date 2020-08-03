# encoding=utf-8

import time
from multiprocessing import Process, Pool
import os
import psutil
import os
import gc
info = psutil.virtual_memory()


# class Test_Multiprocessing:

#    def __init__(self, corenum, threads):
#        #self.cal = int(cal)
#        self.corenum = int(corenum)
#        self.threads = int(threads)

def plusplus(num3):
    result = num3 * num3
    return result


def Test_multicore(i):
    poolTest = Pool(i)
    # for i in range(0, 2):
    #    print(i)
    # for j in range(2):
    #    print(j)
    # startTime_1 = time.time()
    k = 0
    num0 = []
    num1 = []
    for k in range(10):
        # num0 += [plusplus(k)]
        print(k)
        poo2 = poolTest.apply_async(plusplus, (k,))
        print(type(poo2))
        num0.append(poo2)
        num1 += [poo2]
        print(num0)
        print(type(num0))
        print(num1)
        print(type(num1))
        #print(poo2)
    # print('Eddy', num0)
    # pool_result_multicore2 = poolTest.map(plusplus, num0)
    for r in num0:
        print('result', r.get())
    poolTest.close()
    poolTest.join()
    # endTime_1 = time.time()
    #print(pool_result_multicore2)
    #return pool_result_multicore2

    # print(pool_result_multicore)
    # print("time1 :", endTime_1 - startTime_1)
    # print("start1,end1", startTime_1, endTime_1)
    # for m in pool_result_multicore:
    #    print(m)
    # print("start1,end1", startTime_1,endTime_1)
    # print("time1 :", endTime_1 - startTime_1)


def Test_normal(i):
    # startTime_2 = time.time()
    num = []
    for _ in range(i):
        m = 0
        for m in range(10000000):
            # plusplus(l)
            num += [plusplus(m)]
    print(num)
    return num
    # endTime_2 = time.time()
    # print("start2,end2", startTime_2, endTime_2)
    # print("time2 :", endTime_2 - startTime_2)


if __name__ == "__main__":
    #x = Test_Multiprocessing()
    # Test_Multiprocessing.Test_multicore()
    print('è¨˜æ†¶é«”ä½¿?¨ï?', psutil.Process(os.getpid()).memory_info().rss)
    print('ç¸½è??¶é?ï¼?, info.total)
    print('è¨˜æ†¶é«”ä?æ¯”ï?', info.percent)
    print('cpu?‹æ•¸ï¼?, psutil.cpu_count())
    #print(gc.isenabled())
    print(gc.collect())
    Time_1 = time.time()
    Test_multicore(8)
    Time_2 = time.time()
    Test_normal(8)
    Time_3 = time.time()
    print('T1:', Time_2 - Time_1)
    print('T2:', Time_3 - Time_2)
