import matplotlib.pyplot as plt

font1 = {'family': 'serif',
         'color': 'b',
         'weight': 'bold',
         'size': 14
         }

font2 = {'family': 'fantasy',
         'color': 'deeppink',
         'weight': 'normal',
         'size': 'xx-large'
         }
                                                    # 폰트 저장해줌. ‘family’, ‘color’, ‘weight’, ‘size’와 같은 속성을 사용해서 축 레이블 텍스트를 설정
plt.plot([1, 2, 3, 4], [2, 3, 5, 10])
plt.xlabel('X-Axis', labelpad=15, fontdict=font1)   # X-axis 이라고 x축 레이블 지정, 15pt 만큼 여백 지정, 폰트1 불러옴
plt.ylabel('Y-Axis', labelpad=20, fontdict=font2)   # Y-axis 이라고 y축 레이블 지정, 15pt 만큼 여백 지정, 폰트2 불러옴
plt.show()