# matplotlib.pyplot 모듈의 plot()은 선 (Line) 또는 마커 (Marker) 그래프 그리기에 사용되는 함수

import matplotlib.pyplot as plt

data_dict = {'data_x': [1, 2, 3, 4, 5], 'data_y': [2, 3, 5, 10, 8]} # 딕셔너리와 같이 레이블이 있는 데이터를 그래프로 나타낼 수 있음

plt.plot('data_x', 'data_y', data=data_dict)
plt.show()