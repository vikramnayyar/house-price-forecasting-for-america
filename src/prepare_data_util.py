"""

The script declare the functions used in prepare_data.py 

"""
#import pathlib
import pandas as pd
from logzero import logger, logfile
import matplotlib.pyplot as plt

#import numpy as np
#import scipy
#import scipy.stats as stats

#from utility import create_log, parse_config, read_data


def stationarity_test(df):
    
    import matplotlib.pyplot as plt
    from statsmodels.tsa.stattools import adfuller

    #Determining rolling statistics
    rolstd = df.rolling(12).std()
    
    # Plot rolling statistics:
    plt.plot(df, color='blue',label='Original')
    plt.plot(df, color='red', label='Rolling Mean')
    plt.plot(rolstd, color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean and Standard Deviation')
    plt.xlabel('Date')
#    plt.show(block=False)
    plt.savefig("stationarity_test.png")
    
    logger.info("Results of Dickey Fuller Test")
    adft = adfuller(df, autolag='AIC')

    output = pd.Series(adft[0:4],index=['Test Statistics','p-value','No. of lags used','Number of observations used'])
    for key,values in adft[4].items():
        output['critical value (%s)'%key] =  values
    logger.info(output)
    

def decompose_series(df):
    from statsmodels.tsa.seasonal import seasonal_decompose

    
    result = seasonal_decompose(df, model='multiplicative', period = 30)
    fig = plt.figure()  
    fig = result.plot()  
    fig.set_size_inches(16, 9)
    

    fig.suptitle("Series Decomposition of House Prices")
    plt.xlabel('Date')
    plt.savefig("decompose_series.png")

import numpy as np

def remove_trend(df):

#    rcParams['figure.figsize'] = 10, 6
    df_log = np.log(df)
    moving_avg = df_log.rolling(12).mean()
    std_dev = df_log.rolling(12).std()
    
    fig = plt.figure()
    fig.set_size_inches(10, 6)
    
    plt.legend(loc='best')
    plt.title('Moving Average')
    plt.plot(std_dev, color ="black", label = "Standard Deviation")
    plt.plot(moving_avg, color="red", label = "Mean")
    plt.legend()
#    plt.show()
    plt.savefig("moving_average.png")
    return df_log


def split_data(df_log): 
    train_data, test_data = df_log[3:int(len(df_log)*0.9)], df_log[int(len(df_log)*0.9):]
    plt.figure(figsize=(10,6))
    plt.grid(True)
    plt.xlabel('Dates')
    plt.ylabel('Closing Prices')
    plt.plot(df_log, 'green', label='Train data')
    plt.plot(test_data, 'blue', label='Test data')
    plt.legend()
    plt.savefig("train-test-series.png")
    
    
    
    return train_data, test_data