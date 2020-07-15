# encoding=utf-8
from win32com.client import Dispatch
import os
import time
import pandas as pd
import datetime
import time
from csv import DictWriter


class Test_Modem:

    def __init__(self, input_file_directory, input_filename, output_file_directory, output_file_name, log_type,
                 qxxm_summary_filter, qxxm_name_filter, qxxm_itemtype_filter):
        self.input_file_directory = str(input_file_directory)
        self.input_filename = str(input_filename)
        self.output_file_directory = str(output_file_directory)
        self.output_file_name = str(output_file_name)
        self.log_type = str(log_type)
        self.qxxm_summary_filter = str(qxxm_summary_filter)
        self.qxxm_name_filter = str(qxxm_name_filter)
        self.qxxm_itemtype_filter = qxxm_itemtype_filter

    def QXXM_itemType(self, qxxm_itemtype_filter):
        if self.qxxm_itemtype_filter == 6:
            return 'MSG'
        elif self.qxxm_itemtype_filter == 5:
            return 'LOG'

    def QXXT_Logging_Packet(self):
        INPUT_FILE = self.input_file_directory + self.input_filename
        OUTPUT_FILE = self.output_file_directory + self.output_file_name
        QcatApp = win32com.client.Dispatch("QCAT6.Application")
        print("QCAT version: " + QcatApp.AppVersion)
        print("Open Log: " + INPUT_FILE)
        if QcatApp.OpenLog(INPUT_FILE) != 1:
            print("Open Log Error")
            exit()
        print("file open ok")
        # TargetLogIdF = 0xB0C0
        TargetLogIdF = int(self.log_type, 16)
        print(TargetLogIdF)
        print(type(TargetLogIdF))
        # print(TargetLogIdF)
        # print(type(TargetLogIdF))
        SIBFilter = QcatApp.PacketFilter
        SIBFilter.SetAll(False)
        SIBFilter.Set(TargetLogIdF, True)  # Filter 0xB0C0
        SIBFilter.Commit()

        QcatPacketNum = QcatApp.PacketCount  # Total packets
        print(QcatPacketNum)
        # QcatPacket = QcatApp.FirstPacket  # First Packet
        # print(QcatPacket)
        # print(type(QcatPacket.text))
        # print("Test_Eddy:" + str(QcatPacket.Type))
        QcatPacket_2 = QcatApp.ParsePackets(0, 10000)
        # Qcat_title = QcatApp.Name
        # print(Qcat_title)
        # print(type(Qcat_title))
        print(QcatPacket_2)
        print(type(QcatPacket_2))
        QcatApp.SaveAsText(OUTPUT_FILE)

        # Qcatworkspace = QcatApp.Workspace
        # Qcatworkspace.ExportToText('C:\\Users\\Shawn\\Desktop\\tmp\\22.csv',False)
        # Q2 = QcatPacket.Next()  # Next Packet
        # Q2.text  # 获取QCAT解码的内容
        # print(type(Q2))
        # print(Q2)

    def QXXM_Logging_Packet(self):
        j = 0
        print(os.getcwd())
        print(x.QXXM_itemType(6))
        INPUT_FILE = self.input_file_directory + self.input_filename
        # OUTPUT_FILE = self.output_file_directory + self.output_file_name
        QxdmApp = Dispatch("QXDM.QXDMAutoApplication")  # Initialize QXXM
        autoWindow = QxdmApp.GetAutomationWindow()
        print("QXDM version: " + autoWindow.AppVersion)
        print("Open Log: " + INPUT_FILE)
        handle = autoWindow.LoadItemStore(INPUT_FILE)  # load ISF file
        total_itemcounts = autoWindow.GetItemCount()  # Get item counts of the ISF file
        print(total_itemcounts)
        # strNumber = input('PLease setup the number:\n')
        # item = autoWindow.GetItem(handle, strNumber)
        # summary = item.GetItemSummary()
        # print(summary)
        for i in range(0, total_itemcounts):
            item = autoWindow.GetItem(handle, i)
            itemtype = str(item.GetItemType())
            name = item.GetItemName()
            summary = item.GetItemSummary()
            stamp = str(int(item.GetItemTimestamp()))
            keyText = item.GetItemKeyText()
            # act_time = time.localtime(stamp)
            # timeStr = time.strftime("%Y-%m-%d%H:%M:%S",act_time)
            # print(timeStr)
            # print(summary)
            if self.qxxm_itemtype_filter is 5 or 6:
                if self.qxxm_summary_filter in summary and self.qxxm_name_filter in name:
                    j = j + 1
                    print('Eddy_j:', j)
                    print(x.QXXM_itemType(self.qxxm_itemtype_filter) + ' || ' + stamp + ' || ' + name + ' || ' + summary + ' || ' + keyText)
                    data_flag = {
                        'type': [x.QXXM_itemType(self.qxxm_itemtype_filter)],
                        'name': [name],
                        'summary': [summary]
                    }
                    df = pd.DataFrame(data_flag, columns=['type','name', 'summary'])
                    print(df)
                    if j == 1:
                        df.to_csv('test666.csv', mode='a', index=0, header=True)
                    else:
                        df.to_csv('test666.csv', mode='a', index=0, header=False)


#                   with open('test123.csv', 'w', newline='') as csvFile:
#                       fieldnames = ['log_timestamp', 'log_summary', 'log_keytext']
#                       writer = csv.DictWriter(csvFile, fieldnames)
#                       writer.writeheader()
#                       writer.writerow(stamp, summary, keyText)
#               else:
#                   with open('test123.csv', 'a', newline='') as csv:
#                       fieldnames = ['log_timestamp', 'log_summary', 'log_keytext']
#                       writer = csv.DictWriter(csvFile, fieldnames)
#                       writer.writerow(stamp, summary, keyText)


# df_timestamp = [stamp]
# df_summary = [summary]
# df_keytext = [keyText]
# dic = {'log_timestamp':df_timestamp, 'log_summary':df_summary, 'log_keytext':df_keytext}
# df_dic = pd.DataFrame(dic)
# df_dic.to_csv('C:\\Users\\Shawn\\Desktop\\tmp\\test1.csv')

# summary_2 = summary.AddSearchContent(1)
# summary_2 = summary.SetSearchString('CELL_CFG')
# print(summary_2.SetSearchString('CELL_CFG'))


if __name__ == '__main__':
    x = Test_Modem('C:\\Users\\Shawn\\Desktop\\tmp\\', 'log01.isf', 'C:\\Users\\Shawn\\Desktop\\tmp\\', 'log02_isf.txt',
                   '0xB0C0', '=CM=', 'Call Manager/High', 6)
    # print('Input_File_directory:', x.input_file_directory)
    # print('Input_File_name:', x.input_filename)
    # print('Output_File_directory:', x.output_file_directory)
    # print('Output_File_name:', x.output_file_name)
    # print('Filter_Type:', x.log_type)
    # print(type(x.log_type))
    # x.QCAT_Logging_Packet()
    x.QXXM_Logging_Packet()
