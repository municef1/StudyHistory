def solution(lottos, win_nums):
  price = {
    0 : 6,
    1 : 6,
    2 : 5,
    3 : 4,
    4 : 3,
    5 : 2,
    6 : 1,
  }
  worst = len(set(lottos).intersection(set(win_nums)))      # 교집합 개수 구함
  if 0 in lottos:
      best = worst + lottos.count(0)                       
      return[price[best], price[worst]]
  else:
      return[price[worst], price[worst]]