# coding:utf-8
import os
import time
import pandas

package_name = "com.ss.android.ugc.aweme"
# 内存
class Perf_Test():
    def mem_test(self):
        ret_info = os.popen("adb shell dumpsys meminfo %s" % package_name).readlines()
        for pss_info_line in ret_info:
            if pss_info_line.count("TOTAL:") > 0:
                pss_value = pss_info_line.split(":")[1].split("TOTAL")[0].lstrip().rstrip()
                print(pss_value)
        pss_value_list = []
        pss_value_list.append(pss_value)
        pss = pandas.DataFrame(pss_value_list)
        pss.to_csv("pss_2.csv", index=False, sep=',', mode='a', header=False)

# CPU
    def cpu_test(self):
        cpu_info = os.popen("adb shell dumpsys cpuinfo %s" % package_name).readlines()
        for cpu_info_line in cpu_info:
            if cpu_info_line.count("TOTAL:") > 0:
                cpu_value = cpu_info_line.split("TOTAL")[0].lstrip().rstrip()
                print(cpu_value)

        cpu_value_list = []
        cpu_value_list.append(cpu_value)
        cpu = pandas.DataFrame(cpu_value_list)
        cpu.to_csv("cpu_2.csv", index=False, sep=',', mode='a', header=False)

# 电池

    def battery_test(self):
        battery_info = os.popen("adb shell dumpsys battery").readlines()
        for battery_info_line in battery_info:
            if "level" in battery_info_line:
                battery_value = battery_info_line.split(":")[1].lstrip().rstrip()
                print(battery_value)
        battery_value_list = []
        battery_value_list.append(battery_value)
        battery = pandas.DataFrame(battery_value_list)
        battery.to_csv("battery_2.csv", index=False, sep=',', mode='a', header=False)


way=Perf_Test()
while 1:
    way.mem_test()
    way.battery_test()
    way.cpu_test()
    time.sleep(3)




