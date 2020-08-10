# encoding=utf-8

import time
from multiprocessing import Process, Pool
import os
import psutil
import os
import gc
import pandas as pd
import numpy as np

info = psutil.virtual_memory()
csv_log_time = time.localtime()
output_filename = 'Test_' + time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime()) + '.csv'
output_filename_r = 'Test_R_' + time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime()) + '.csv'
output_filename_s = 'Test_S_' + time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime()) + '.csv'


# output_filename_2 = 'Test_c_' + time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime()) + '.csv'

def kill_process():
    PROCNAME = "QXDM.exe"
    print(psutil.process_iter())
    for proc in psutil.process_iter():
        # check whether the process name matches
        print(proc.name())
        if proc.name() == PROCNAME:
            proc.kill()


# class Test_Multiprocessing:

#    def __init__(self, corenum, threads):
#        #self.cal = int(cal)
#        self.corenum = int(corenum)
#        self.threads = int(threads)
def get_local_time_info(val):
    time_ticket = time.strftime('%Y-%m-%d_%H-%M-%S', val)
    return time_ticket


def listtoarray():
    test0 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    arr0 = np.array(test0)
    print(arr0)
    print(type(arr0))


def listtostring():
    test0 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    print(type(test0))
    print(test0)
    str0 = ','.join(test0)
    str1 = ''.join(test0)
    str2 = ' '.join(test0)
    print(str0)
    print(str1)
    print(str2)


def arraytolist():
    test0 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    arr0 = np.array(test0)
    test1 = arr0.tolist()
    print(test1)


def arraytostring():
    test0 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    arr0 = np.array(test0)
    test1 = arr0.tolist()
    test2 = ','.join(test1)
    print(test1)
    print(test2)


def arraytoint():
    test0 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    arr0 = np.array(test0)
    print(arr0)
    # test1 = arr0.tolist()
    # test2 = ' '.join(test1)
    # print(test2)
    print(len(arr0))
    print(type(int(arr0[0])))
    print(type(arr0[0]))
    for j in range(len(arr0)):
        print(arr0[j])


#    test1 = test0.tolist()
#    print(test1)
#    test2 = ''.join(test1)
#   print(test2)


def plusplus(num3):
    global output_filename
    result = num3 * num3
    summary = str(num3 * num3) + '_test_verification'
    data = {'result': [result],
            'summary': [summary]
            }
    df = pd.DataFrame(data, columns=['result', 'summary'])
    df.to_csv(output_filename, mode='a', index=0, header=False)

    # return result


def plusplus_r(num3):
    global output_filename
    result = num3 * num3
    summary = str(num3 * num3) + '_test_verification'
    # data = {'result': [result]
    #        }
    df = pd.DataFrame(result)
    df.to_csv(output_filename_r)


def plusplus_s(num3):
    global output_filename
    # result = np.array(['test123', 'rrr'])
    # result = np.array(['1', '2', '3', '4', '5'])
    result = num3 * num3
    # print(num3)
    # print(type(num3))
    # result = np.array(num3.tolist())
    # teststring = 'eddy_love_test_verification'
    # teststringtoArray = np.array(list(teststring))
    # print(teststringtoArray)
    # print(type(teststringtoArray))
    ## summary = np.append(result, teststringtoArray)
    # summary = np.char.add(result, teststring)
    summary = np.add(result, [10])
    print(summary)
    # summary = num3 * num3
    # data = {
    #    'summary': [summary]
    # }
    df = pd.DataFrame(summary)
    df.to_csv(output_filename_s)


def plusplus_r_txt(num3):
    global output_filename
    result = num3 * num3
    print(result)
    str = result.tostring()
    print(str)
    print(np.fromstring(str, dtype=int))


def testifori():
    test0 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
    arr0 = np.array(test0)
    t = [i for i in range(len(arr0))]
    print(t)
    print(type(t))


# f = open('testtest.txt', 'w')
# f.writelines(result)
# f.close()
# summary = str(num3 * num3) + '_test_verification'
# data = {'result': [result]
#        }
# df = pd.DataFrame(data, columns=['result', 'summary'])
# df.to_csv(output_filename_r, mode='a', index=0, header=False)


#

def plusplus_s_txt(num3):
    global output_filename
    summary = str(num3 * num3) + '_test_verification'
    print(summary)
    f = open('testtest_s.txt', 'w')
    f.writelines(summary)
    f.close()
    # summary = str(num3 * num3) + '_test_verification'
    # data = {
    #    'summary': [summary]
    # }
    # df = pd.DataFrame(data, columns=['result', 'summary'])
    # df.to_csv(output_filename_s, mode='a', index=0, header=False)


def Test_multicore(i):
    global output_filename
    poolTest = Pool(i)
    # for i in range(0, 2):
    #    print(i)
    # for j in range(2):
    #    print(j)
    # startTime_1 = time.time()
    k = 0
    num0 = []
    num1 = []
    for k in range(100000):
        # num0 += [plusplus(k)]
        print(k)
        poo2 = poolTest.apply_async(plusplus, (k,))
        # print(type(poo2))
        num0.append(poo2)
        num1 += [poo2]
        # print(num0)
        # print(type(num0))
        # print(num1)
        # print(type(num1))
        #print(poo2)
    # print('Eddy', num0)
    # pool_result_multicore2 = poolTest.map(plusplus, num0)
    # for r in num0:
    #     print('result', r.get())
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


def Test_np_multiprocess():
    k = np.arange(0, 100000, 1)
    print(k)
    # print(type(k))
    # for k in range(1000):
    # num0 = []
    #    print(k)
    poo2a = Process(target=plusplus_r, args=(k,))
    poo2b = Process(target=plusplus_s, args=(k,))
    #    # print(type(poo2))
    # num0.append(poo2a)
    # num0.append(poo2b)
    poo2a.run()
    poo2b.run()


def Test_fr_multiprocess():
    t = []
    for k in range(10000):
        t.append(k)
        print(t)
        # print(type(t))


def Test_multiprocess():
    # global output_filename
    # poolTest = Pool(i)
    # for i in range(0, 2):
    #    print(i)
    # for j in range(2):
    #    print(j)
    # startTime_1 = time.time()
    # k = 0
    num0 = []
    # num1 = []
    for k in range(100000):
        # num0 += [plusplus(k)]
        print(k)
        poo2a = Process(target=plusplus_r, args=(k,))
        poo2b = Process(target=plusplus_s, args=(k,))
        # print(type(poo2))
        num0.append(poo2a)
        num0.append(poo2b)
        poo2a.run()
        poo2b.run()
        # num1 += [poo2]
        # print(num0)
        # print(type(num0))
        # print(num1)
        # print(type(num1))
        # print(poo2)
    # print('Eddy', num0)
    # pool_result_multicore2 = poolTest.map(plusplus, num0)
    # for r in num0:
    #     print('result', r.get())
    # poolTest.close()
    # poolTest.join()
    # endTime_1 = time.time()
    # print(pool_result_multicore2)
    # return pool_result_multicore2

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
        for m in range(500000):
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
    print(psutil.Process(os.getpid()).memory_info().rss)
    print(info.total)
    print(info.percent)
    print(psutil.cpu_count())
    #print(gc.isenabled())
    # print(gc.collect())
    # Time_1 = time.time()
    # df0 = pd.DataFrame(columns=['result', 'summary'])
    # df0.to_csv(output_filename_r, mode='a', index=0, header=True)
    # df0.to_csv(output_filename_s, mode='a', index=0, header=True)
    # Test_multiprocess()
    # Time_2 = time.time()
    # df0.to_csv(output_filename, mode='a', index=0, header=True)
    # Test_multicore(8)
    # Time_3 = time.time()
    # print('T1:', Time_2 - Time_1)
    # print('T2:', Time_3 - Time_2)

    #######################################
    Time_1 = time.time()
    # Test_np_multiprocess()
    # listtoarray()
    # listtostring()
    # arraytolist()
    # arraytostring()
    # arraytoint()
    # testifori()
    kill_process()
    Time_2 = time.time()
    # Test_multicore
    Time_3 = time.time()
    print('T1:', Time_2 - Time_1)
    print('T2:', Time_3 - Time_2)
#
