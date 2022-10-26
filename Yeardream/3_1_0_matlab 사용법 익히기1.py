# pyplot.plot() 함수에 하나의 숫자 리스트를 입력함으로써 아래와 같은 그래프가 그려집니다.

# plot() 함수는 리스트의 값들이 y 값들이라고 가정하고, x 값 [0, 1, 2, 3]을 자동으로 만들어냅니다.

# matplotlib.pyplot 모듈의 show() 함수는 그래프를 화면에 나타나도록 합니다.

import matplotlib.pyplot as plt

plt.plot([1, 2, 3, 4])
plt.show()