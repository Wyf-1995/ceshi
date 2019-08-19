#-*- encoding: utf-8 -*-

import os
import time
import pandas

package_name = "com.ss.android.ugc.aweme"

class PerfRecorder():

    @classmethod
    def get_pss_info(cls):
        ret_info = os.popen("adb shell dumpsys meminfo %s" % package_name).readlines()
        for pss_info_line in ret_info:
            if pss_info_line.count("TOTAL:") > 0:
                pss_value = pss_info_line.split(":")[1].split("TOTAL")[0].lstrip().rstrip()
                print(pss_value)
                return pss_value
        # pss_value_list = []
        # pss_value_list.append(pss_value)
        # pss=pandas.DataFrame(list)
        # pss.to_csv("pss.csv",index=False,sep=',',mode='a',header=False)

    @classmethod
    def get_cpu_info(cls):
        cpu_info = os.popen("adb shell dumpsys cpuinfo %s" % package_name).readlines()
        for cpu_info_line in cpu_info:
            if cpu_info_line.count("TOTAL:") > 0:
                cpu_value = cpu_info_line.split("TOTAL")[0].lstrip().rstrip()
                print(cpu_value)
                return cpu_value

    #
    @classmethod
    def get_battry_info(cls):
        battery_info = os.popen("adb shell dumpsys battery").readlines()
        for battery_info_line in battery_info:
            if "level" in battery_info_line:
                battery_value = battery_info_line.split(":")[1].lstrip().rstrip()
                print(battery_value)
                return battery_value


    # @classmethod
    # def get_fps_info(cls):
    #     fps_value=[]
    #     fps_info = os.popen("adb shell dumpsys gfxinfo %s"%package_name).readlines()
    #     for fps_info_line in fps_info:
    #         print(type(fps_info_line))
    #         if "Draw" in fps_info_line:
    #             for i in range(len(fps_info_line)+1):
    #                 fps_value.append(fps_info_line[i])
                # fps_value = fps_info_line.split(":")[1].lstrip().rstrip()
                # print(fps_value)
                # return fps_value



class PerfRunner():

    pss_value_list = []
    cpu_value_list = []
    battery_value_list = []
    fps_info_list = []

    def run(self):
        for i in range(30):
            time.sleep(1)
            pss_info = PerfRecorder.get_pss_info()
            cpu_info = PerfRecorder.get_cpu_info()
            battery_info = PerfRecorder.get_battry_info()
            # fps_info = PerfRecorder.get_fps_info()

            self.pss_value_list.append(pss_info)
            self.cpu_value_list.append(cpu_info)
            self.battery_value_list.append(battery_info)
            # self.fps_info_list.append(fps_info)
    # pss = pandas.DataFrame(pss_value_list)
    # pss.to_csv("pss.csv", index=False, sep=',', mode='a', header=False)


#
#     @property
#     def perf_data(self):
#         perf_result_dic = {
#             "pss": self.pss_value_list,
#             "cpu": self.cpu_value_list,
#             # "fps": self.fps_info_list,
#             "battery": self.battery_value_list
#         }
#         return perf_result_dic
#         print(perf_result_dic)
#
#
#
if __name__ == '__main__':
#     # 1. 启动性能测试采集器
    per_runner = PerfRunner()
    per_runner.run()
#
#     # 2. 生成csv报告
#     ReportHelper.gen_csv_report(per_runner.perf_data)