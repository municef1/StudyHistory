from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.linear_model import Lasso
from sklearn.ensemble import RandomForestRegressor
from lightgbm.sklearn import LGBMRegressor
from xgboost import XGBRegressor 
from sklearn import svm

def train_val_split(X, y):
    # 트테트테
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2,
                                                    random_state=42)
    # print(X_train.shape, X_val.shape, y_train.shape, y_val.shape)
    return X_train, X_val, y_train, y_val



def Linear_reg(X_train, X_val, y_train, y_val):
    reg = LinearRegression()
    reg.fit(X_train, y_train)
    pred = reg.predict(X_train) 
    print("\n\n----- Training -----")
    print("\n--- Linear Regression ---")
    print("RMSE : %.4f" % mean_squared_error(y_train, pred)**0.5)
    print("R2 : %.4f" % r2_score(y_train, pred))

    result = reg.predict(X_val) 
    print("\n----- Predict -----")
    print("\n--- Linear Regression ---")
    print("RMSE : %.4f" % mean_squared_error(y_val, result)**0.5)
    print("R2 : %.4f" % r2_score(y_val, result))


def ridge(X_train, X_val, y_train, y_val):
    reg2 = Ridge()
    reg2.fit(X_train, y_train)
    pred2 = reg2.predict(X_train)
    print("\n\n----- Training -----")
    print("\n--- Ridge ---")
    print("RMSE : %.4f" % mean_squared_error(y_train, pred2)**0.5)
    print("R2 : %.4f" % r2_score(y_train, pred2))

    result2 = reg2.predict(X_val)
    print("\n----- Predict -----")
    print("\n--- Ridge ---")
    print("RMSE : %.4f" % mean_squared_error(y_val, result2)**0.5)
    print("R2 : %.4f" % r2_score(y_val, result2))


def lasso(X_train, X_val, y_train, y_val):
    reg3 = Lasso()
    reg3.fit(X_train, y_train)
    pred3 = reg3.predict(X_train) 
    print("\n\n\n----- Training -----")
    print("\n--- Lasso ---")
    print("RMSE : %.4f" % mean_squared_error(y_train, pred3)**0.5)
    print("R2 : %.4f" % r2_score(y_train, pred3))

    result3 = reg3.predict(X_val) 
    print("\n----- Predict -----")
    print("\n--- Lasso ---")
    print("RMSE : %.4f" % mean_squared_error(y_val, result3)**0.5)
    print("R2 : %.4f" % r2_score(y_val, result3))


def RF(X_train, X_val, y_train, y_val):
    reg4 = RandomForestRegressor()
    reg4.fit(X_train, y_train)
    pred4 = reg4.predict(X_train)
    print("\n\n----- Training -----")
    print("\n---  Random Forest ---")
    print("RMSE : %.4f" % mean_squared_error(y_train, pred4)**0.5)
    print("R2 : %.4f" % r2_score(y_train, pred4))

    result4 = reg4.predict(X_val)
    print("\n----- Predict -----")
    print("\n---  Random Forest ---")
    print("RMSE : %.4f" % mean_squared_error(y_val, result4)**0.5)
    print("R2 : %.4f" % r2_score(y_val, result4))



def XGB(X_train, X_val, y_train, y_val):
    reg5 = XGBRegressor()
    reg5.fit(X_train, y_train)
    pred5 = reg5.predict(X_train) 
    print("\n\n----- Training -----")
    print("\n--- XGBoost ---")
    print("RMSE : %.4f" % mean_squared_error(y_train, pred5)**0.5)
    print("R2 : %.4f" % r2_score(y_train, pred5))

    result5 = reg5.predict(X_val) 
    print("\n----- Predict -----")
    print("\n--- XGBoost ---")
    print("RMSE : %.4f" % mean_squared_error(y_val, result5)**0.5)
    print("R2 : %.4f" % r2_score(y_val, result5))




def LGB(X_train, X_val, y_train, y_val):
    # reg6 = LGBMRegressor(objective='regression',n_estimators=876,
    #                      max_depth=14,learning_rate=0.0041615,
    #                      min_child_samples=17, subsample=0.4702824)
    reg6 = LGBMRegressor()
    reg6.fit(X_train, y_train)
    pred6 = reg6.predict(X_train)
    print("\n\n----- Training -----")
    print("\n--- LGBM --")
    print("RMSE : %.4f" % mean_squared_error(y_train, pred6)**0.5)
    print("R2 : %.4f" % r2_score(y_train, pred6))

    result6 = reg6.predict(X_val)
    print("\n----- Predict -----")
    print("\n--- LGBM --")
    print("RMSE : %.4f" % mean_squared_error(y_val, result6)**0.5)
    print("R2 : %.4f" % r2_score(y_val, result6))




def svr(svr_kernel, X_train, X_val, y_train, y_val):
    reg7 = svm.SVR(kernel=svr_kernel)
    reg7.fit(X_train, y_train)
    # pred7 = reg7.predict(X_train)
    print("\n\n----- Training -----")
    print("\n--- SVR --")
    # print("RMSE : %.4f" % mean_squared_error(y_train, pred7)**0.5)
    print("R2 : %.4f" % reg7.score(X_train, y_train))

    # result7 = reg7.predict(X_val)
    # print("\n----- Predict -----")
    # print("\n--- SVR --")
    # # print("RMSE : %.4f" % mean_squared_error(y_val, result7)**0.5)
    # print("R2 : %.4f" % reg7.score(y_val, result7))