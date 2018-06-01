import pandas as pd # 판다스 사용
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import font_manager, rc
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
'''
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
print(traffic_union_table)
traffic_union_table.to_csv("2016/2016서울역.txt",mode='w', encoding='euc-kr')
'''

filename ='2016/2016서울역.txt'

#data = pd.read_csv(filename, encoding='CP949', index_col=0, header=0, engine='python')
data = np.loadtxt(filename, delimiter=',')
time=data[:,0]
traffic_in=data[:,1]
traffic_out=data[:,2]

plt.figure(num=1,dpi=100,facecolor='white')
plt.plot(time,traffic_in, color="blue", linewidth=2.5, linestyle="--", label="승차")
plt.plot(time,traffic_out,'r-', label="하차")

plt.title('서울역2016(1분류)')
plt.xlabel('시간')
plt.ylabel('인원')
plt.xlim(5,25)
plt.ylim(0,7000)
#plt.xticks(np.arange(0,5.5,0.5))
plt.grid()
plt.legend()

plt.savefig("2016/서울역.png",dpi=300)
plt.show()
