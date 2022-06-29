import pandas as pd

def load_data():
    data = pd.read_csv('./data/train_ppr.csv')
    return data

def load_train():
    train = pd.read_csv('./data/train.csv')
    train = train.rename(columns={'송하인_격자공간고유번호':'send','수하인_격자공간고유번호':'rec','물품_카테고리':'cat','운송장_건수':'cnt'})
    train= train.drop(columns='index')
    return train

def load_test():
    test = pd.read_csv('./data/test.csv')
    test = test.rename(columns={'송하인_격자공간고유번호':'send','수하인_격자공간고유번호':'rec','물품_카테고리':'cat'})
    test= test.drop(columns='index')
    return test

def load_submission():
    submission = pd.read_csv('./data/sample_submission.csv')
    return submission

