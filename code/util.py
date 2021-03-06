import time
from functools import wraps
import pickle
import os
import config
import numpy as np
import pandas as pd


def timethis(func):
    """
    Decorator that reports the execution time.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Function", func.__name__, "costs", end-start, "sec.")
        return result
    return wrapper
    
    
def saveit(df, fname):
    """
    Save pd.DataFrame to csv file and pickle file.
    """
    csvname, pklname = fname + '.csv', fname + '.pkl'
    df.to_csv(os.path.join('tmp2', csvname))
    if config.DEBUG is True:
        return
    with open(os.path.join('tmp2', pklname), 'wb') as f:
        pickle.dump(df, f, -1)


def loadit(fname):
    """
    Load obj from pickle file.
    """
    pklname = fname + '.pkl'
    with open(os.path.join('tmp2', pklname), 'rb') as f:
        obj = pickle.load(f) 
    return obj


def loadcsv(fname):
    """
    Load df from csv file.
    """
    csvname = fname + '.csv'
    df = pd.read_csv(os.path.join('tmp2', csvname), index_col=0)
    return df
                                  

def dumpit(obj, fname):
    """
    Dump the obj using pickle.
    """
    pklname = fname + '.pkl'
    with open(os.path.join('tmp2', pklname), 'wb') as f:
        pickle.dump(obj, f, -1)
               

def submit(ypred):
    from dataloader import DataLoader
    dataloader = DataLoader(config) 
    df_test = dataloader.load_test_data()
    id_test = df_test['id']
    pd.DataFrame({"id": id_test, "relevance": ypred}).to_csv('submission.csv',index=False)
    
    
    
    
