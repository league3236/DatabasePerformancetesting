import pandas as pd # 판다스 사용
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from matplotlib import font_manager, rc
import matplotlib.pylab as pylab
params = {'legend.fontsize': 20,
          'figure.figsize': (10, 7),
         'axes.labelsize': 25,
         'axes.titlesize':30,
         'xtick.labelsize':20,
         'ytick.labelsize':20}
pylab.rcParams.update(params)

font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
'''
stationname_list_0 = ['강변','개롱','개화산','건대입구','고덕','고려대','고속터미널','김포공항','노원','녹사평','당산',
                      '대치','독립문','동대문','동작','마장','마포구청','망원', '모란','발산','사당',
                      '상수','성신여대입구','송정','신당','신도림','신천','신촌','안암','약수','어린이대공원','영등포시장',
                      '오목교','올림픽공원','왕십리','용두','월드컵경기장','이대','이수','이촌','이태원','일원','잠실','장지',
                      '제기동','종합운동장','천호','청량리','총신대입구','학여울','한성대입구','혜화','홍대입구']
stationname_list_1 = ['가락시장','강동구청','공덕','광흥창','구로디지털단지','남구로','남태령','내방','대흥','도곡','도림천',
                      '디지털미디어시티','뚝섬','마곡','마포','매봉','몽촌토성','문래','문정','반포','방배','방이','버티고개',
                      '보라매','복정','상왕십리','서울역','석촌','성수','송파','수서','숙대입구','신길','신설동','애오개',
                      '양평','영등포구청','오금','장한평','청구','충정로','합정','효창공원앞']
stationname_list_2 = ['강동','거여','공릉','광나루','광명사거리','구산','구의','구파발','군자','굽은다리','금호','길동','길음',
                      '까치산','낙성대','남성','남한산성입구','녹번','단대오거리','답십리','당고개','대림','대청','도봉산','독바위',
                      '돌곶이','둔촌동','뚝섬유원지','마들','마천','먹골','면목','명일','목동','무악재','미아','미아사거리','방화',
                      '보문','봉천','봉화산','불광','사가정','산성','상계','상도','상봉','상일동','새절','서울대입구','석계','수락산',
                      '수유','수진','숭실대입구','신금호','신답','신대방','신대방삼거리','신림','신정','신정네거리','신풍','신흥',
                      '쌍문','아차산','아현','암사','양천구청','역촌','연신내','옥수','온수','용답','용마산','우장산','월곡','응암','잠원',
                      '장승배기','장암','중계','중곡','중화','증산','지축','창동','창신','철산','태릉입구','하계','행당','홍제',
                      '화곡','화랑대']
stationname_list_3 = ['가산디지털단지','강남','강남구청','경복궁','광화문','교대','남부터미널','논현','동대문역사문화공원','동대입구',
                      '동묘앞','명동','삼각지','삼성','서대문','서초','선릉','시청','신사','신용산','안국','압구정','양재','여의나루',
                      '여의도','역삼','을지로3가','을지로4가','을지로입구','종각','종로3가','종로5가','청담','충무로','학동','한강진',
                      '한양대','회현']
'''
stationname_list_0 = ['Daechi','Dongjak']
stationname_list_1 = ['Gangdong-gu Office','Mapo']
stationname_list_2 = ['Kkachisan','Sanggye']
stationname_list_3 = ['Gasan Digital Complex','Yeouido']
#동대문(0),잠실(0),강동(2)나,뚝섬(1),마곡(1)나,마포(1)나,서울역(1),신길(1),강동(2)나,미아(2),
# 금호(2),신대방(2),신정(2)나,강남(3),삼성(3),시청(3),압구정(3),양재(3) 는 따로 조사해야함.
#변경해야 할 내용
year = '10'
filename =year+'.txt'
stationname = '신정'
stationname_bar = stationname#+'\('
bunryu = '3'
#변경해야 할 내용 끝
#리스트에 있는 것을 뽑으려면 아래 for문으로 돌려야함

for stationname in stationname_list_3:
    print(stationname)
    traffic_table = pd.read_csv(filename, encoding='CP949', index_col=0, header=0)
    #print(traffic_table[traffic_table['역명']=='서울역(*'])
    traffic_table=traffic_table[traffic_table['역명'].str.contains(stationname)]   #특정 단어를 포함하는 것만 검출
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
    print("가공전")
    print(traffic_in_table)

    traffic_in_table = traffic_in_table.mean()
    traffic_out_table=traffic_out_table.mean()
    print("가공후")
    print(traffic_in_table)


    traffic_union_table = pd.concat([traffic_in_table,traffic_out_table], axis=1)   #최종적으로 승차랑 하차랑 합침
    traffic_union_table = traffic_union_table.drop("역번호")
    traffic_union_table = traffic_union_table.rename(columns={ 1: 0})
    #traffic_union_table.columns.values[0:0] = "시간"
    print(traffic_union_table)

    stationfilename =year+'/'+year+stationname+'.txt'
    traffic_union_table.to_csv(stationfilename,mode='w', encoding='euc-kr')
    #메모장 읽어와서 첫번째 줄만 삭제하기
    with open(stationfilename, 'r') as fin:
        data1 = fin.read().splitlines(True)
    with open(stationfilename, 'w') as fout:
        fout.writelines(data1[1:])

    #이곳은 그래프 그려서 저장시키는 소스
    #data = pd.read_csv(stationfilename, encoding='CP949', index_col=0, header=0, engine='python')
    data = np.loadtxt(stationfilename, delimiter=',')
    time=data[:,0]
    traffic_in=data[:,1]
    traffic_out=data[:,2]

    plt.figure(num=1,dpi=100,facecolor='white')
    plt.plot(time,traffic_in, color="blue", linewidth=2.5, linestyle="--", label="boarding")
    plt.plot(time,traffic_out,'r-', label="alighting")

    plt.title(stationname)
    plt.xlabel('hour')
    plt.ylabel('number of passengers')
    plt.xlim(5,25)
    plt.ylim(0)
    #plt.xticks(np.arange(0,5.5,0.5))
    plt.grid()
    plt.legend()

    plt.savefig(year+"/"+bunryu+"/"+stationname+".png",dpi=300)
    plt.clf() #그래프를 초기화 한다
'''
print(stationname)
traffic_table = pd.read_csv(filename, encoding='CP949', index_col=0, header=0)
# print(traffic_table[traffic_table['역명']=='서울역(*'])
traffic_table = traffic_table[traffic_table['역명']==stationname]  # 특정 단어를 포함하는 것만 검출
#traffic_table=traffic_table[traffic_table['역명'].str.contains(stationname_bar)]
traffic_in_table = []  # 승차
traffic_out_table = []  # 하차
traffic_union_table = []  # 승차 합차 합치기
traffic_in_table = traffic_table[traffic_table['구분'] == '승차']  # 승차만 저장
traffic_out_table = traffic_table[traffic_table['구분'] == '하차']  # 하차만 저장

traffic_in_table = traffic_in_table.mean()

traffic_out_table = traffic_out_table.mean()

traffic_union_table = pd.concat([traffic_in_table, traffic_out_table], axis=1)  # 최종적으로 승차랑 하차랑 합침
traffic_union_table = traffic_union_table.drop("역번호")
traffic_union_table = traffic_union_table.rename(columns={1: 0})
print(traffic_union_table)

stationfilename = '2016/2016' + stationname + '.txt'
traffic_union_table.to_csv(stationfilename, mode='w', encoding='euc-kr')
# 메모장 읽어와서 첫번째 줄만 삭제하기
with open(stationfilename, 'r') as fin:
    data1 = fin.read().splitlines(True)
with open(stationfilename, 'w') as fout:
    fout.writelines(data1[1:])

# 이곳은 그래프 그려서 저장시키는 소스
data = np.loadtxt(stationfilename, delimiter=',')
time = data[:, 0]
traffic_in = data[:, 1]
traffic_out = data[:, 2]

plt.figure(num=1, dpi=100, facecolor='white')
plt.plot(time, traffic_in, color="blue", linewidth=2.5, linestyle="--", label="승차")
plt.plot(time, traffic_out, 'r-', label="하차")

plt.title(stationname + '2016(' + bunryu + '분류)')
plt.xlabel('시간')
plt.ylabel('인원')
plt.xlim(5, 25)
plt.ylim(0)
plt.grid()
plt.legend()

plt.savefig("2016/" + stationname + ".png", dpi=300)
plt.show()
plt.clf()  # 그래프를 초기화 한다
'''
