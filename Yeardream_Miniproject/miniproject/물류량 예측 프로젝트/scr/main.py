
from dataloader import *
from preprocess import *
from model import *



train = load_train()

train = over_10_drop(train)  # target >10 drop
# over_10_to_10(train)         # target >10  to 10
# over_10_to_step(train)         # target categorical


train_x , train_y = code_split(train)


# category_split(train_x)  # 카테고리 10개로 축소
category_split_2(train_x) # 카테고리 10개로 축소한것 추가 (카테고리 컬럼 2개)

label_encoding(train_x)
# train_x = ohencoding(train_x)

print(train_x)

X_train, X_val, y_train, y_val = train_val_split(train_x, train_y)


Linear_reg(X_train, X_val, y_train, y_val)
ridge(X_train, X_val, y_train, y_val)
lasso(X_train, X_val, y_train, y_val)
RF(X_train, X_val, y_train, y_val)
XGB(X_train, X_val, y_train, y_val)
LGB(X_train, X_val, y_train, y_val)
# svr('linear',X_train, X_val, y_train, y_val)


'''
데이콘 제출 시 코드

reg6 = LGBMRegressor()
reg6.fit(train_x, train_y)

test = load_test()

test['s1-5'] = test.loc[:,'send'].astype(str).str[:5]
test['s6-9'] = test.loc[:,'send'].astype(str).str[5:9]
test['s10'] = test.loc[:,'send'].astype(str).str[9]
test['s11-16'] = test.loc[:,'send'].astype(str).str[10:]
test['r1-5'] = test.loc[:,'rec'].astype(str).str[:5]
test['r6-9'] = test.loc[:,'rec'].astype(str).str[5:9]
test['r10'] = test.loc[:,'rec'].astype(str).str[9]
test['r11-16'] = test.loc[:,'rec'].astype(str).str[9:]

test = test.drop(columns=['send','rec'])

label_encoding(test)

submission = load_submission()

result = reg6.predict(test)
submission['운송장_건수'] = result
submission.reset_index(drop=True).to_csv("submission.csv", index=False)
'''