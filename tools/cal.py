###########################################
# 这个工具用来合并一对单向流量,形成站点之间的总OD流量
###########################################

import csv,json

data = []
from_station=[]

arr = [5,5,4,8,7,5,5,7,6,4]
r=[]
i = 0
while i < len(arr):
    j = i + 1
    while j < len(arr):
        if arr[i] == arr[j]:
            i += 1
            j = i
            # j = i + 1
        j+=1
    r.append(arr[i])
    i+=1

# for i in range(0, len(arr)):
#     for j in range(i + 1,len(arr)):
#         if arr[i] == arr[j]:
#             i += 1
#             j = i
#     r.append(arr[i])


with open('../data/OD.csv','r',encoding='utf_8') as csvfile:
    raw = csv.reader(csvfile)
    next(csvfile)

    for row in raw:
        data.append({
            'fstation': row[0],
            'tstation': row[1],
            'value': row[2]
        })

for row in data:
    if row['fstation'] not in from_station:
        from_station.append(row['fstation'])

to_station = from_station.copy()

icount=0
# with open('res.csv','w',encoding='utf_8') as f:
#     w = csv.writer(f)
#
#     for f in from_station:
#         for t in to_station:
#             l = [x for x in data if
#                  (x['fstation'] == f and x['tstation'] == t) or
#                  (x['fstation'] == t and x['tstation'] == f)]
#
#             if len(l) == 2:
#                 res = [l[0]['fstation'],l[0]['tstation'],int(l[0]['value'])+int(l[1]['value'])]
#                 data.remove(l[1])
#                 data.remove(l[0])
#             elif len(l) == 1:
#                 res = [l[0]['fstation'],l[0]['tstation'],int(l[0]['value'])]
#                 data.remove(l[0])
#
#             if len(l) > 0:
#                 icount+=1
#                 print(icount)
#                 w.writerow(res)
jr = {}
with open('res_csv.csv','w',encoding='utf_8',newline='') as csvout:
    w = csv.writer(csvout)
    w.writerow(['FROM_STATION','TO_STATION','FLOW'])

    for f in from_station:
        jr[f] = []

        for t in to_station:
            l = [x for x in data if
                 (x['fstation'] == f and x['tstation'] == t) or
                 (x['fstation'] == t and x['tstation'] == f)]

            if len(l) == 2:
                res = [f,t,int(l[0]['value'])+int(l[1]['value'])]
                data.remove(l[1])
                data.remove(l[0])
            elif len(l) == 1:
                res = [f,t,int(l[0]['value'])]
                data.remove(l[0])

            if len(l) > 0:
                icount+=1
                print(icount)
                # jr[f][res[1]]= res[2]
                # if res[2] > 3000:
                jr[f].append({
                    res[1]: res[2]
                })
                w.writerow(res)

# with open('res.csv','w',encoding='gbk') as f:
#     json.dump(jr, f, ensure_ascii=False)


# 把字典转成列表
arr = []
for k,v in jr.items():
    arr.append({
        'ZDMC': k,
        'LINK': v
    })

with open('res_f.json','w',encoding='utf_8') as f:
    json.dump(arr, f, ensure_ascii=False)

print("转换完成！")






