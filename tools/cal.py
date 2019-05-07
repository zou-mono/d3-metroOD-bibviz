import csv

data = []
from_station=[]

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
with open('res.csv','w',encoding='utf_8') as f:
    w = csv.writer(f)

    for f in from_station:
        for t in to_station:
            l = [x for x in data if
                 (x['fstation'] == f and x['tstation'] == t) or
                 (x['fstation'] == t and x['tstation'] == f)]

            if len(l) == 2:
                res = [l[0]['fstation'],l[0]['tstation'],int(l[0]['value'])+int(l[1]['value'])]
                data.remove(l[1])
                data.remove(l[0])
            elif len(l) == 1:
                res = [l[0]['fstation'],l[0]['tstation'],int(l[0]['value'])]
                data.remove(l[0])

            if len(l) > 0:
                icount+=1
                print(icount)
                w.writerow(res)




