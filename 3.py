#pithon 문자열을 python 으로 수정
a = 'pithon'
a[:1]
'p'
a[2:]
'thon'
a[:1] + 'y' + a[2:]
'python'

print(a[:1] + 'y' + a[2:]) # 이런식으로 문자열 수정은 슬라이싱을 사용하기