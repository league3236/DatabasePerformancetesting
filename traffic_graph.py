import pandas as pd # 판다스 사용
import numpy as np
import matplotlib.pyplot as plt
filename ='2016.txt'

traffic_table = pd.read_csv(filename, encoding='CP949', index_col=0, header=0)
#print(traffic_table[traffic_table['역명']=='서울역(*'])
traffic_table=traffic_table[traffic_table['역명'].str.contains('서울역\(')]   #특정 단어를 포함하는 것만 검출
#print(traffic_table)
traffic_in_table = []   #승차
traffic_out_table = []   #하차
traffic_union_table = [] #승차 합차 합치기
traffic_in_table = traffic_table[traffic_table['구분']=='승차'] #승차만 저장
#print(traffic_in_table)
traffic_out_table = traffic_table[traffic_table['구분']=='하차'] #하차만 저장
#print(traffic_out_table)

#traffic_union_table = pd.concat([traffic_in_table,traffic_out_table])   #최종적으로 승차랑 하차랑 합칠 거임.
#print(traffic_union_table)
#traffic_in_table=traffic_in_table.groupby(['구분']).mean()
#traffic_out_table=traffic_out_table.groupby(['구분']).mean()

traffic_in_table=traffic_in_table.mean()

traffic_out_table=traffic_out_table.mean()

traffic_union_table = pd.concat([traffic_in_table,traffic_out_table], axis=1)   #최종적으로 승차랑 하차랑 합침
traffic_union_table = traffic_union_table.drop("역번호")
traffic_union_table = traffic_union_table.rename(columns={'':'시간', 0: '승차', 1: '하차'})
#traffic_union_table.columns.values[0:0] = "시간"

traffic_union_table.to_csv("2016서울역.txt",mode='w', encoding='euc-kr')

times = range(5,24)
pieces = []
for d in traffic_union_table:
    pieces.append(d)

print(d)
