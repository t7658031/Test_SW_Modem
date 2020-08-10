# encoding=utf-8
# import self as self
import win32com
from win32com.client import Dispatch
import os
import time
import pandas as pd
import datetime
import time
from csv import DictWriter
from numba import jit
import time
from multiprocessing import Process, Pool, freeze_support
import gc
import numpy as np
import threading
import psutil

# from multiprocessing.pool import ThreadPool as Pool
# from pathos.multiprocessing import ProcessingPool as Pool
# class Test_Modem:

# def __init__(self, input_file_directory, input_filename, output_file_directory, output_file_name, log_type,
#             qxdm_summary_filter, qxdm_name_filter, qxdm_itemtype_filter, csv_name):
#    self.input_file_directory = str(input_file_directory)
#    self.input_filename = str(input_filename)
#    self.output_file_directory = str(output_file_directory)
#    self.output_file_name = str(output_file_name)
#    self.log_type = str(log_type)
#    self.qxdm_summary_filter = str(qxdm_summary_filter)
#    self.qxdm_name_filter = str(qxdm_name_filter)
#    self.qxdm_itemtype_filter = qxdm_itemtype_filter
#    self.csv_name = str(csv_name) + '.csv'
input_file_directory = 'F:\\Pycharm\\Project\\Test_Modem\\'
val1 = 'test0810.txt'
val2 = 15
val3 = 'ENL2DL   | NR | Last   2000 ms'
# val3 = '=CM='
val4 = 'Call Manager/High'
user_itemtype = 15
user_summary = str(val3)
user_name = str(val4)
PROCNAME = "QXDM.exe"


# txt_path0 = 'F:\\Pycharm\\Project\\Test_Modem\\07-30_12-19.txt'
# output_filename_timestamp = str(val1)[:-4] + '_Trf_' + time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime()) + '.txt'


# val5 = QXDM_itemCounts(val1)
# INPUT_FILE = input_file_directory + val1


def get_local_time_info(val):
    time_ticket = time.strftime('%Y-%m-%d_%H-%M-%S', val)
    return time_ticket


# def QXDM_itemType(val):
#    if val == 6:
#        return 'MSG'
#    elif val == 5:
#        return 'LOG'
#    elif val == -1:
#        return ''
#    elif val == 15:
#        return 'QTRACE'


##def QXDM_itemCounts(val):
#   input_file_directory = 'F:\\Pycharm\\Project\\Test_Modem\\'
#   input_filename = str(val)
#   INPUT_FILE = input_file_directory + input_filename
#   # OUTPUT_FILE = self.output_file_directory + self.output_file_name
#   QxdmApp = Dispatch("QXDM.QXDMAutoApplication")  # Initialize QXDM
#   autoWindow = QxdmApp.GetAutomationWindow()
#   print("QXDM version: " + autoWindow.AppVersion)
#   print("Open Log: " + INPUT_FILE)
#   handle = autoWindow.LoadItemStore(INPUT_FILE)  # load ISF file
#   # global total_itemcounts
#   total_itemcounts = autoWindow.GetItemCount()  # Get item counts of the ISF file
#   print(total_itemcounts)
#   return total_itemcounts


def QXDM_Logging_Packet_TestMode(obj_qxdmitem):
    # print('tp0001')
    # print(obj_qxdmitem)
    # Announce
    # input_file_directory = 'F:\\Pycharm\\Project\\Test_Modem\\'
    # output_file_directory = 'F:\\Pycharm\\Project\\Test_Modem\\'
    # csv_log_time = time.localtime()
    # input_filename = str(val01)
    # output_filename = str(val1)[:-4] + '_' + get_local_time_info(csv_log_time) + '.csv'
    # user_itemtype = val02
    # user_summary = str(val03)
    # user_name = str(val04)
    # total_caps = val05
    # print('output_filename:', output_filename)
    # j = 0
    # INPUT_FILE = input_file_directory + input_filename
    # print(os.getcwd())
    # print(x.QXDM_itemType(6))
    # OUTPUT_FILE = self.output_file_directory + self.output_file_name
    # Start
    # QxdmApp = Dispatch("QXDM.QXDMAutoApplication")  # Initialize QXDM
    # autoWindow = QxdmApp.GetAutomationWindow()
    # print("QXDM version: " + autoWindow.AppVersion)
    # print("Open Log: " + INPUT_FILE)
    # handle = autoWindow.LoadItemStore(INPUT_FILE)  # load ISF file
    ## global total_itemcounts
    # total_itemcounts = autoWindow.GetItemCount()  # Get item counts of the ISF file
    # print(total_itemcounts)
    # strNumber = input('PLease setup the number:\n')
    # item = autoWindow.GetItem(handle, strNumber)
    # summary = item.GetItemSummary()
    # print(summary)
    # if total_caps == total_itemcounts:
    # for i in range(0, total_itemcounts):
    #    item = autoWindow.GetItem(handle, i)
    itemtype = str(obj_qxdmitem.GetItemType())
    # global itemtype_global
    # itemtype_global= item.GetItemType()
    name = obj_qxdmitem.GetItemName()
    summary = obj_qxdmitem.GetItemSummary()
    stamp = int(obj_qxdmitem.GetItemTimestamp())
    stamp_f = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stamp / 1000))
    # keyText = obj_item.GetItemKeyText()
    # act_time = time.localtime(stamp)
    # timeStr = time.strftime("%Y-%m-%d%H:%M:%S",act_time)
    # print(timeStr)
    # print(summary)
    # print(self.qxdm_itemtype_filter)
    # print(itemtype)
    # print('Counter i:', i)
    if user_itemtype == 6:
        # print('TP_01')
        # print(user_name, user_summary)
        if user_summary in summary:
            # j = j + 1
            # print('Eddy_j:', j)
            # print(itemtype + ' || ' + QXDM_itemType(user_itemtype) + ' || ' + stamp_f + ' || ' +
            #      name + ' || ' + summary)
            print(itemtype + ' || ' + stamp_f + ' || ' +
                  name + ' || ' + summary)
            data_flag = {
                'type': [itemtype],
                'time_stamp': [stamp_f],
                'name': [name],
                'summary': [summary]
            }
            # df_qxdm = pd.DataFrame(data_flag, columns=['type', 'filter', 'name', 'summary'])
            df_qxdm = pd.DataFrame(data_flag, columns=['type', 'time_stamp', 'name', 'summary'])
            # print('eddy_qx1:', df_qxdm)
            # print('eddy_qx2:', type(df_qxdm))
            # print(data_flag)
            # return data_flag #輸出字典
            # return data_flag
            # if i > 0:
            #    df_qxdm.to_csv(output_filename, mode='a', index=0, header=True)
            # else:
            # df_qxdm.to_csv(output_filename, mode='a', index=0, header=False)
        elif user_itemtype == -1:
            # print('TP_02')
            # if self.qxdm_summary_filter in summary and self.qxdm_name_filter in name:
            # j = j + 1
            # print('Eddy_j:', j)
            print(itemtype + ' || ' + stamp_f + ' || ' + name + ' || ' + summary)
            data_flag = {
                'type': [itemtype],
                'time_stamp': [stamp_f],
                'name': [name],
                'summary': [summary]
            }
            df = pd.DataFrame(data_flag, columns=['type', 'time_stamp', 'name', 'summary'])
            # print(df)
            # if j == 1:
            #    df.to_csv(output_filename, mode='a', index=0, header=True)
            # else:
            # df.to_csv(output_filename, mode='a', index=0, header=False)
        elif user_itemtype == 15:
            # print('TP_03')
            if int(itemtype) == 15:
                if user_summary in summary:
                    # j = j + 1
                    # print('Eddy_Counter:', j)
                    print(itemtype + ' || ' + stamp_f + ' || ' + name + ' || ' + summary)
                    data_flag = {
                        'type': [itemtype],
                        'time_stamp': [stamp_f],
                        'name': [name],
                        'summary': [summary]
                    }
                    df = pd.DataFrame(data_flag, columns=['type', 'time_stamp', 'name', 'summary'])
                    # print(df)
                    # if j == 1:
                    #     df.to_csv(output_filename, mode='a', index=0, header=True)
                    # else:
                    # df.to_csv(output_filename, mode='a', index=0, header=False)
    # df_timestamp = [stamp]


def QXDM_Time_Summary_Api(val):
    print('val:', val)
    QxdmApp = Dispatch("QXDM.QXDMAutoApplication")  # Initialize QXDM
    autoWindow = QxdmApp.GetAutomationWindow()
    handle = autoWindow.LoadItemStore(INPUT_FILE)  # load ISF file
    for k in range(len(val)):
        val_T = val[k]
        print(val_T)
        # time.sleep(0.5)
        # try:
        obj_item = autoWindow.GetItem(handle, val_T)
        print(obj_item)
        if obj_item is None:
            print('Eddy_obj:', obj_item)
        itemtype = str(obj_item.GetItemType())
        name = obj_item.GetItemName()
        summary = obj_item.GetItemSummary()
        stamp = int(obj_item.GetItemTimestamp())
        stamp_f = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stamp / 1000))
        # itemtype = str(obj_item.GetItemType())
        # except:
        #    print('Exception')
        # else:
        if user_itemtype == 6:
            if user_summary in summary:
                # print(itemtype + ' || ' + stamp_f + ' || ' +
                #      name + ' || ' + summary)
                print(stamp_f + ' || ' + summary)
                # data_1 = np.array([stamp_f])
                # data_2 = np.array([summary])
                # data_npflag = np.append(data_1, data_2)
                # print(data_npflag)
                # df = pd.DataFrame(data_npflag, columns=['time_stamp', 'summary'])
                # df.to_csv(output_filename_timestamp, mode='a', index=0, header=False)
                data_flag = {
                    'time_stamp': [stamp_f],
                    'summary': [summary]
                }
                df_qxdm_1 = pd.DataFrame(data_flag, columns=['time_stamp', 'summary'])
                df_qxdm_1.to_csv(output_filename_timestamp, mode='a', index=0, header=False)
        elif user_itemtype == 15:
            if int(itemtype) == 15:
                if user_summary in summary:
                    # print(itemtype + ' || ' + stamp_f + ' || ' + name + ' || ' + summary)
                    data_flag = {
                        # 'type': [itemtype],
                        'time_stamp': [stamp_f],
                        # 'name': [name],
                        'summary': [summary]
                    }
                    df_qxdm_1 = pd.DataFrame(data_flag, columns=['time_stamp', 'summary'])
                    df_qxdm_1.to_csv(output_filename_timestamp, mode='a', index=0, header=False)


def QXDM_log_reader(txt_path):
    df = pd.read_fwf(txt_path)
    print(df)


def QXDM_log_Trf(val_i, val_o):
    # df = pd.read_fwf(txt_path)
    # print(df)
    ##df_todic = df.to_dict('list')
    ##print(df_todic)
    # df1 = df.to_csv('test1011.csv', mode='a', index=0, header=False)
    # print(df1)
    cp = open(val_i, "r", encoding="utf-8")
    fp = open(val_o, "a")
    # line_count = len(cp.readlines())
    # print('tag1:', line_count)
    cp_lines = cp.readlines()
    for i in range(len(cp_lines)):
        # i += 1
        j = i - 1
        if val3 in cp_lines[i]:
            print(type(cp_lines[i]))
            print('tag4:', cp_lines[j] + cp_lines[i])
            fp.write(cp_lines[j] + cp_lines[i])

        # print('tag2:', i)
        # print('tag3:', cp_lines[i], i)
        # print('tag4:', cp_lines[i])
    fp.close()
    cp.close()


# for ci in range(line_count):
#     print(ci)
#     print(cp_lines[ci])
# fp = open(txt_path0, "r")
# for li in iter(fp):
#     #print(li)
#     if val3 in li:
#         print(li)
# cp.close()

# def QXDM_Symmary_Api(obj):
#    itemtype = str(obj.GetItemType())
#    name = obj.GetItemName()
#    summary = obj.GetItemSummary()
#    stamp = int(obj.GetItemTimestamp())
#    stamp_f = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stamp / 1000))
#    if user_itemtype == 6:
#        if user_summary in summary:
#            # print(itemtype + ' || ' + stamp_f + ' || ' +
#            #      name + ' || ' + summary)
#            # print(stamp_f + ' || ' + summary)
#            data_flag = {
#                'summary': [summary]
#            }
#            df_qxdm_2 = pd.DataFrame(data_flag, columns=['time_stamp', 'summary'])
#            df_qxdm_2.to_csv(output_filename_summary, mode='a', index=0, header=False)
#    elif user_itemtype == 15:
#        print('itemtype:', itemtype)
#        if int(itemtype) == 15:
#            if user_summary in summary:
#                # print(itemtype + ' || ' + stamp_f + ' || ' + name + ' || ' + summary)
#                data_flag = {
#                    # 'type': [itemtype],
#                    # 'time_stamp': [stamp_f],
#                    # 'name': [name],
#                    'summary': [summary]
#                }
#                df_qxdm_2 = pd.DataFrame(data_flag, columns=['time_stamp', 'summary'])
#                df_qxdm_2.to_csv(output_filename_summary, mode='a', index=0, header=False)


# def QXDM_Logging_Packet_Multiprocessing(self):
#    pool = Pool()
#    num0 = []
#    for k in range(0, 10000):
#        num0 += [k]
#    print(num0)
#    pool_result_multicore2 = pool.map(Test_Modem.QXDM_Logging_Packet_TestMode, num0)
#    pool.close()
#    pool.join()
#    print(pool_result_multicore2)
#    return pool_result_multicore2


# df_summary = [summary]
# df_keytext = [keyText]
# dic = {'log_timestamp':df_timestamp, 'log_summary':df_summary, 'log_keytext':df_keytext}
# df_dic = pd.DataFrame(dic)
# df_dic.to_csv('C:\\Users\\Shawn\\Desktop\\tmp\\test1.csv')

# summary_2 = summary.AddSearchContent(1)
# summary_2 = summary.SetSearchString('CELL_CFG')
# print(summary_2.SetSearchString('CELL_CFG'))


if __name__ == '__main__':
    INPUT_FILE = input_file_directory + val1
    csv_log_time = time.localtime()
    output_filename_timestamp = str(val1)[:-4] + '_info_' + get_local_time_info(csv_log_time) + '.txt'
    # output_filename_summary = str(val1)[:-4] + '_summary_' + get_local_time_info(csv_log_time) + '.csv'
    # df0 = pd.DataFrame(columns=['time_stamp', 'summary'])
    # df0.to_csv(output_filename_timestamp, mode='a', index=0, header=True)
    # QxdmApp = Dispatch("QXDM.QXDMAutoApplication")  # Initialize QXDM
    # autoWindow = QxdmApp.GetAutomationWindow()
    # print("QXDM version: " + autoWindow.AppVersion)
    # print("Open Log: " + INPUT_FILE)
    # handle = autoWindow.LoadItemStore(INPUT_FILE)  # load ISF file
    # total_itemcounts = autoWindow.GetItemCount()  # Get item counts of the ISF file
    # print('Total_caps:', total_itemcounts)
    Time_1 = time.time()
    # print(QXDM_log_reader(txt_path0))
    # print(QXDM_log_Trf(txt_path0))
    print(QXDM_log_Trf(val1, output_filename_timestamp))
    # print('Time1:', Time_1)
    # i = np.arange(0, total_itemcounts, 1)
    # process_Test_time = Process(target=QXDM_Time_Summary_Api, args=(i,))
    # # time.sleep(1)
    # #for proc in psutil.process_iter():
    # #    # print('TP_kill')
    # #    # check whether the process name matches
    # #    if proc.name() == PROCNAME:
    # #        print('TP_kill')
    # #        proc.kill()
    # process_Test_time.run()
    Time_2 = time.time()
    print('Time1:', Time_1)
    print('Time2:', Time_2)
    print('T1:', Time_2 - Time_1)

# poolTest = Pool()
# pool_result_multicore2 = poolTest.map(QXDM_Logging_Packet_TestMode, eddy_poolcounts)
# poolTest.close()
# poolTest.join()
#
# df = pd.DataFrame(QXDM_Logging_Packet_TestMode(obj_item), columns=['type', 'filter', 'name', 'summary'])
# print(df)
# if i > 0:
#    #    df.to_csv(output_filename, mode='a', index=0, header=True)
#    # else:
#    df.to_csv(output_filename, mode='a', index=0, header=False)

# itemtype = str(item.GetItemType())

# pool.map(QXDM_Logging_Packet_TestMode('log01.isf', 6, '=CM=', 'Call Manager/High', QXDM_itemCounts('log01.isf')), urls)
# QXDM_Logging_Packet_TestMode('log01.isf', 6, '=CM=', 'Call Manager/High', QXDM_itemCounts('log01.isf'))
# print()
# QXDM_itemCounts('log01.isf')
# print(QXDM_itemType(5))

# x = Test_Modem('F:\\Pycharm\\Project\\Test_Modem\\', 'log02.isf', 'F:\\Pycharm\\Project\\Test_Modem\\',
#               'log03_isf.txt', '0xB0C0', 'enl2_dl_qsh.c    931', 'QSH/ANALYSIS/Low/ENL2DL', 15, 'test000')
# x = Test_Modem('F:\\Pycharm\\Project\\Test_Modem\\', 'log01.isf', 'F:\\Pycharm\\Project\\Test_Modem\\',
#               'log01_isf.txt', '0xB0C0', '=CM=', 'Call Manager/High', 6, 'test1113')
# print(x.QXDM_itemType(6))
## m = x.QXDM_itemCounts()
## print('Test_Eddy_m:', m)
## x.QXDM_Logging_Packet_Multiprocessing()
# pool = Pool()
# num0 = [10000]
## for k in range(0, 10000):
##    num0 += [k]
## print(num0)
# pool_result_multicore2 = pool.map(x.QXDM_Logging_Packet_TestMode, num0)
# pool.close()
# pool.join()
# print("TestE:", pool_result_multicore2)
## print('Input_File_directory:', x.input_file_directory)
# print('Input_File_name:', x.input_filename)
# print('Output_File_directory:', x.output_file_directory)
# print('Output_File_name:', x.output_file_name)
# print('Filter_Type:', x.log_type)
# print(type(x.log_type))
# m = x.QXDM_itemCounts()
# print(type(m))
# print(m)
# x.QXDM_Logging_Packet_TestMode(m)
# print(x.qxdm_itemtype_filter)
# print(type(x.qxdm_itemtype_filter))
#    poolTest = Pool(8)
# x.QXDM_Logging_Packet_TestMode()
#    num0 = []
#   for k in range(m):
#        num0 += [k]
# pool_result_multicore2 = poolTest.map(x.QXDM_Logging_Packet_TestMode, num0)
# print(pool_result_multicore2)
