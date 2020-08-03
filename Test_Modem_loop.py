# encoding=utf-8
import self as self
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
from multiprocessing import Process, Pool


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


def get_local_time_info(val):
    time_ticket = time.strftime('%Y-%m-%d_%H-%M-%S', val)
    return time_ticket


def QXDM_itemType(val):
    if val == 6:
        return 'MSG'
    elif val == 5:
        return 'LOG'
    elif val == -1:
        return ''
    elif val == 15:
        return 'QTRACE'


def QXDM_itemCounts(val):
    input_file_directory = 'F:\\Pycharm\\Project\\Test_Modem\\'
    input_filename = str(val)
    INPUT_FILE = input_file_directory + input_filename
    # OUTPUT_FILE = self.output_file_directory + self.output_file_name
    QxdmApp = Dispatch("QXDM.QXDMAutoApplication")  # Initialize QXDM
    autoWindow = QxdmApp.GetAutomationWindow()
    print("QXDM version: " + autoWindow.AppVersion)
    print("Open Log: " + INPUT_FILE)
    handle = autoWindow.LoadItemStore(INPUT_FILE)  # load ISF file
    # global total_itemcounts
    total_itemcounts = autoWindow.GetItemCount()  # Get item counts of the ISF file
    print(total_itemcounts)
    return total_itemcounts


def QXDM_Logging_Packet_TestMode(val01, val02, val03, val04, val05):
    # Announce
    input_file_directory = 'F:\\Pycharm\\Project\\Test_Modem\\'
    output_file_directory = 'F:\\Pycharm\\Project\\Test_Modem\\'
    csv_log_time = time.localtime()
    input_filename = str(val01)
    output_filename = str(val01)[:-4] + '_' + get_local_time_info(csv_log_time) + '.csv'
    user_itemtype = val02
    user_summary = str(val03)
    user_name = str(val04)
    total_caps = val05
    print('output_filename:', output_filename)
    j = 0
    INPUT_FILE = input_file_directory + input_filename
    # print(os.getcwd())
    # print(x.QXDM_itemType(6))
    # OUTPUT_FILE = self.output_file_directory + self.output_file_name
    # Start
    QxdmApp = Dispatch("QXDM.QXDMAutoApplication")  # Initialize QXDM
    autoWindow = QxdmApp.GetAutomationWindow()
    print("QXDM version: " + autoWindow.AppVersion)
    print("Open Log: " + INPUT_FILE)
    handle = autoWindow.LoadItemStore(INPUT_FILE)  # load ISF file
    # global total_itemcounts
    total_itemcounts = autoWindow.GetItemCount()  # Get item counts of the ISF file
    print(total_itemcounts)
    # strNumber = input('PLease setup the number:\n')
    # item = autoWindow.GetItem(handle, strNumber)
    # summary = item.GetItemSummary()
    # print(summary)
    if total_caps == total_itemcounts:
        for i in range(0, total_itemcounts):
            item = autoWindow.GetItem(handle, i)
            print('E-item:', item)
            print('E-item_type:', type(item))
            itemtype = str(item.GetItemType())
            # global itemtype_global
            # itemtype_global= item.GetItemType()
            name = item.GetItemName()
            summary = item.GetItemSummary()
            stamp = int(item.GetItemTimestamp())
            stamp_f = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(stamp / 1000))
            keyText = item.GetItemKeyText()
            # act_time = time.localtime(stamp)
            # timeStr = time.strftime("%Y-%m-%d%H:%M:%S",act_time)
            # print(timeStr)
            # print(summary)
            # print(self.qxdm_itemtype_filter)
            # print(itemtype)
            print('Counter i:', i)
            if user_itemtype == 5 or user_itemtype == 6:
                # print('TP_01')
                # print(user_name, user_summary)
                if user_summary in summary and user_name in name:
                    j = j + 1
                    print('Eddy_j:', j)
                    print(itemtype + ' || ' + QXDM_itemType(user_itemtype) + ' || ' + stamp_f + ' || ' +
                          name + ' || ' + summary)
                    data_flag = {
                        'type': [itemtype],
                        'filter': [QXDM_itemType(user_itemtype)],
                        'name': [name],
                        'summary': [summary]
                    }
                    df = pd.DataFrame(data_flag, columns=['type', 'filter', 'name', 'summary'])
                    print(df)
                    if j == 1:
                        df.to_csv(output_filename, mode='a', index=0, header=True)
                    else:
                        df.to_csv(output_filename, mode='a', index=0, header=False)
            elif user_itemtype == -1:
                # print('TP_02')
                # if self.qxdm_summary_filter in summary and self.qxdm_name_filter in name:
                j = j + 1
                print('Eddy_j:', j)
                print(itemtype + ' || ' + QXDM_itemType(
                    user_itemtype) + ' || ' + stamp_f + ' || ' + name + ' || ' + summary)
                data_flag = {
                    'type': [itemtype],
                    'name': [name],
                    'summary': [summary]
                }
                df = pd.DataFrame(data_flag, columns=['type', 'name', 'summary'])
                print(df)
                if j == 1:
                    df.to_csv(output_filename, mode='a', index=0, header=True)
                else:
                    df.to_csv(output_filename, mode='a', index=0, header=False)
            elif user_itemtype == 15:
                # print('TP_03')
                if int(itemtype) == 15:
                    if user_name in name and user_summary in summary:
                        j = j + 1
                        print('Eddy_Counter:', j)
                        print(itemtype + ' || ' + QXDM_itemType(user_itemtype) + ' || ' + stamp_f + ' || ' +
                              name + ' || ' + summary)
                        data_flag = {
                            'type': [itemtype],
                            'filter': [QXDM_itemType(user_itemtype)],
                            'name': [name],
                            'summary': [summary]
                        }
                        df = pd.DataFrame(data_flag, columns=['type', 'filter', 'name', 'summary'])
                        print(df)
                        if j == 1:
                            df.to_csv(output_filename, mode='a', index=0, header=True)
                        else:
                            df.to_csv(output_filename, mode='a', index=0, header=False)
        # df_timestamp = [stamp]


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
    input_file_directory = 'F:\\Pycharm\\Project\\Test_Modem\\'
    val1 = 'log01.isf'
    val2 = 6
    val3 = '=CM='
    val4 = 'Call Manager/High'
    val5 = QXDM_itemCounts(val1)
    QXDM_Logging_Packet_TestMode(val1, val2, val3, val4, val5)
    # pool = Pool(processes=4)

    # pool.map(QXDM_Logging_Packet_TestMode('log01.isf', 6, '=CM=', 'Call Manager/High', QXDM_itemCounts('log01.isf')), urls)
    # QXDM_Logging_Packet_TestMode('log01.isf', 6, '=CM=', 'Call Manager/High', QXDM_itemCounts('log01.isf'))
    print()
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
