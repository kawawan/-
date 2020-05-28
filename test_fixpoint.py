import datetime
import pandas as pd
import locale
from pathlib import Path
import numpy as np


dir = input()
#path = 'C:/Program Files (x86)/Apache/Apache24/logs/test.log'
p = Path(dir)
log_list = list(p.glob("*"))

locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')

final_times_cnt = np.array([0 for x in range(0,24)])
final_hostdict = {}
#print(type(log_list))


for log_file in log_list:
    with open(log_file) as f:
        l = f.readlines()

    #時間別
    #    print(type(l))
        times_cnt = [0 for i in range(0,24)]
        access_time_list = []
        for i in range(len(l)):
            time = l[i].split()[3]
            time = time.strip("[")
            time = time[-8:]
            date_dt = datetime.datetime.strptime(time, '%H:%M:%S')
            access_time_list.append(date_dt)

    #    print(access_time_list)

        a = datetime.timedelta(hours= 1)
        b = datetime.timedelta(seconds=1)
        start = datetime.datetime(year=1900,month=1,day=1)
        finish = datetime.datetime(year=1900,month=1,day=1,hour=23)
    #    print(a,b,start,finish)
    #    print(type(start + a * 23),type(date_dt),date_dt)
    #    print(start + a * 0 <= access_time_list[5])


        for i in range(len(access_time_list)):
        #print(access_time_list[i])
            for j in range(0, 24):
            #print(start + a * j, start + a * (j + 1) - b)
                if (start + a * j <= access_time_list[i]):
                    if access_time_list[i] < start + a * (j + 1) - b:
                        times_cnt[j] += 1
    
        times_cnt_np = np.array(times_cnt)
        final_times_cnt = final_times_cnt + times_cnt_np

    # host別
        hostdict = {}
        for i in range(len(l)):
            hostname = l[i].split()[0]
            #print(hostname)
            if not hostname in hostdict:
                hostdict[hostname] = 1
            else:
                hostdict[hostname] += 1

        for k in hostdict:
            if not k in final_hostdict:
                final_hostdict[k] = hostdict[k]
            else:
                final_hostdict[k] = final_hostdict[k] + hostdict[k]
            

print("時間帯別のアクセス数")
for j in range(0,24):
    ltime = start + a * j
    rtime = start + a * (j + 1) - b
    ltime = ltime.time()
    rtime = rtime.time()
    print(ltime, rtime, final_times_cnt[j])

print()
print()

#print(final_hostdict)
final_hostdict_sorted = sorted(final_hostdict.items(), reverse=True)
# print(hostdict_sorted)
print("リモートホスト別")
for host in final_hostdict_sorted:
    print(host[0] + " から " + str(host[1]) + " 回")





