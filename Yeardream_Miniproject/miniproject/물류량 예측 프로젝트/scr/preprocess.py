import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


def over_10_drop(data):
    data = data.drop(data[data['cnt']>10].index)
    return data

def over_10_to_10(data):
    data.loc[data[data['cnt']>10].index,'cnt'] =10

def over_10_to_step(data):
    data.loc[data[(data['cnt']>10) & (data['cnt']<=30)].index,'cnt'] =20
    data.loc[data[(data['cnt']>30) & (data['cnt']<=60)].index,'cnt'] =45
    data.loc[data[(data['cnt']>60) & (data['cnt']<=100)].index,'cnt'] =80
    data.loc[data[data['cnt']>100].index,'cnt'] =150


# 격자고유번호 5/4/1/6
def code_split(data):
    X , y = data.drop(columns='cnt'), data['cnt']

    X['s1-5'] = X.loc[:,'send'].astype(str).str[:5]
    X['s6-9'] = X.loc[:,'send'].astype(str).str[5:9]
    X['s10'] = X.loc[:,'send'].astype(str).str[9]
    X['s11-16'] = X.loc[:,'send'].astype(str).str[10:]
    X['r1-5'] = X.loc[:,'rec'].astype(str).str[:5]
    X['r6-9'] = X.loc[:,'rec'].astype(str).str[5:9]
    X['r10'] = X.loc[:,'rec'].astype(str).str[9]
    X['r11-16'] = X.loc[:,'rec'].astype(str).str[9:]

    X = X.drop(columns=['send','rec'])
    return X, y


# 격자고유번호 5/5/6
def code_split2(data):
    X , y = data.drop(columns='cnt'), data['cnt']

    X['s1-5'] = X.loc[:,'send'].astype(str).str[:5]
    X['s6-10'] = X.loc[:,'send'].astype(str).str[5:10]
    X['s11-16'] = X.loc[:,'send'].astype(str).str[10:]
    X['r1-5'] = X.loc[:,'rec'].astype(str).str[:5]
    X['r6-10'] = X.loc[:,'rec'].astype(str).str[5:10]
    X['r11-16'] = X.loc[:,'rec'].astype(str).str[10:]

    X = X.drop(columns=['send','rec'])
    return X, y




# 카테고리 10가지로 축소
def category_split(data):
    data['cat'] = data['cat'].replace(['아우터', '신발', '상의', '하의', '기타패션의류', '양말/스타킹', '잠옷', '원피스/점프슈트'],0)
    data['cat'] = data['cat'].replace('농산물',1)
    data['cat'] = data['cat'].replace(['수납가구', '아웃도어가구', '카페트/러그', '서재/사무용가구', '주방가구', '침실가구'] , 2)
    data['cat'] = data['cat'].replace(['의료용품', '건강용품', '생활용품', '문구/사무용품', '주방용품', '침구세트', '침구단품', '인테리어소품', '공구', '커튼/블라인드', 'DIY자재/용품', '위생/건강용품', '뷰티소품', '세탁용품', '수납/정리용품', '반려동물', '완구/매트', '홈데코'], 3)
    data['cat'] = data['cat'].replace(['수산', '음료', '기타식품', '건강식품', '가공식품', '축산', '과자', '다이어트식품', '냉동/간편조리식품', '김치', '반찬'], 4)
    data['cat'] = data['cat'].replace(['음반', '문화컨텐츠'], 5)
    data['cat'] = data['cat'].replace(['스킨케어', '헤어케어', '바디케어', '클렌징', '기타화장품/미용', '헤어스타일링', '베이스메이크업', '향수', '선케어', '네일케어', '색조메이크업', '남성화장품', '구강위생용품', '눈관리용품', '욕실용품'], 6)
    data['cat'] = data['cat'].replace(['기저귀/물티슈', '분유/이유식/아기간식', '기타출산/육아', '유아가구', '출산/유아동잡화', '출산/유아동의류'], 7)
    data['cat'] = data['cat'].replace(['기타디지털/가전', '모니터', 'PC', 'PC주변기기', '계절가전', '태블릿PC/노트북액세서리', '스마트디바이스', '스마트디바이스액세서리', '게임기/타이틀', '생활가전', '음향가전', '주방가전', '이미용가전'], 8)
    data['cat'] = data['cat'].replace(['기타스포츠/레저', '등산', '낚시', '스포츠잡화', '캠핑', '헬스', '취미용품', '골프'], 9)
    data['cat'] = data['cat'].replace(['헤어액세서리', '모자', '기타패션잡화', '언더웨어', '패션소품', '선글라스/안경테', '지갑', '기능성', '가방', '헤어액세서리', '주얼리', '자동차용품', '재활운동용품'], 10)
    return data


# 카테고리 전체 100개에 축소한 컬럼 추가
def category_split_2(data):
    data['cat_2'] = data['cat']
    data['cat'] = data['cat'].replace(['아우터', '신발', '상의', '하의', '기타패션의류', '양말/스타킹', '잠옷', '원피스/점프슈트'],0)
    data['cat'] = data['cat'].replace('농산물',1)
    data['cat'] = data['cat'].replace(['수납가구', '아웃도어가구', '카페트/러그', '서재/사무용가구', '주방가구', '침실가구'] , 2)
    data['cat'] = data['cat'].replace(['의료용품', '건강용품', '생활용품', '문구/사무용품', '주방용품', '침구세트', '침구단품', '인테리어소품', '공구', '커튼/블라인드', 'DIY자재/용품', '위생/건강용품', '뷰티소품', '세탁용품', '수납/정리용품', '반려동물', '완구/매트', '홈데코'], 3)
    data['cat'] = data['cat'].replace(['수산', '음료', '기타식품', '건강식품', '가공식품', '축산', '과자', '다이어트식품', '냉동/간편조리식품', '김치', '반찬'], 4)
    data['cat'] = data['cat'].replace(['음반', '문화컨텐츠'], 5)
    data['cat'] = data['cat'].replace(['스킨케어', '헤어케어', '바디케어', '클렌징', '기타화장품/미용', '헤어스타일링', '베이스메이크업', '향수', '선케어', '네일케어', '색조메이크업', '남성화장품', '구강위생용품', '눈관리용품', '욕실용품'], 6)
    data['cat'] = data['cat'].replace(['기저귀/물티슈', '분유/이유식/아기간식', '기타출산/육아', '유아가구', '출산/유아동잡화', '출산/유아동의류'], 7)
    data['cat'] = data['cat'].replace(['기타디지털/가전', '모니터', 'PC', 'PC주변기기', '계절가전', '태블릿PC/노트북액세서리', '스마트디바이스', '스마트디바이스액세서리', '게임기/타이틀', '생활가전', '음향가전', '주방가전', '이미용가전'], 8)
    data['cat'] = data['cat'].replace(['기타스포츠/레저', '등산', '낚시', '스포츠잡화', '캠핑', '헬스', '취미용품', '골프'], 9)
    data['cat'] = data['cat'].replace(['헤어액세서리', '모자', '기타패션잡화', '언더웨어', '패션소품', '선글라스/안경테', '지갑', '기능성', '가방', '헤어액세서리', '주얼리', '자동차용품', '재활운동용품'], 10)
    return data


def label_encoding(data):
    le = LabelEncoder()
    for i in range(len(data.columns)):
        data.iloc[:,i] = le.fit_transform(data.iloc[:,i])

    return data


def ohencoding(train):
    train = train.loc[:,train.columns!='cat'].astype(int)
    train = pd.get_dummies(train)
    return train