"""

The script declare the functions used in prepare_data.py 

"""
import pandas as pd
import numpy as np

from logzero import logger
import matplotlib.pyplot as plt

from statsmodels.tsa.stattools import adfuller

from statsmodels.tsa.seasonal import seasonal_decompose

from utility import parse_config

config_path = "../config/config.yaml"   
config = parse_config(config_path)   # read config file


def stationarity_test(df):

    #Determining rolling statistics
    rolstd = df.rolling(12).std()
    
    # Plot rolling statistics:
    plt.plot(df, color='blue',label='Original')
    plt.plot(df, color='red', label='Rolling Mean')
    plt.plot(rolstd, color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title(config["prepare_data"]["stationarity_test"]["title"] , fontsize = 14)
    plt.xlabel('Date')
    plt.savefig("stationarity_test.png")
    
    logger.info("Results of Dickey Fuller Test")
    adft = adfuller(df, autolag='AIC')

    output = pd.Series(adft[0:4],index=['Test Statistics','p-value','No. of lags used','Number of observations used'])
    for key,values in adft[4].items():
        output['critical value (%s)'%key] =  values
    logger.info(output)
    

def decompose_series(df):
    
    result = seasonal_decompose(df, model='multiplicative', period = 30)
    fig = plt.figure()  
    fig = result.plot()  
    fig.set_size_inches(12, 19)
#    fig.suptitle("Series Decomposition of House Prices", fontsize = 18)
    
    fig.suptitle(config["prepare_data"]["decompose_series"]["title"], fontsize = 18)   
    plt.xlabel(config["prepare_data"]["decompose_series"]["xlabel"])
    plt.savefig("decompose_series.png")


def remove_trend(df):

    df_log = np.log(df)
    moving_avg = df_log.rolling(12).mean()
    std_dev = df_log.rolling(12).std()
    fig = plt.figure()
    fig.set_size_inches(12, 9)
    
    plt.legend(loc='best')
    plt.title('Moving Average', fontsize = 14)
    plt.plot(std_dev, color ="black", label = "Standard Deviation")
    plt.plot(moving_avg, color="red", label = "Mean")
    plt.legend()
    plt.savefig("moving_average.png")
    return df_log


def split_data(df_log): 
    train_data, test_data = df_log[3:int(len(df_log)*0.9)], df_log[int(len(df_log)*0.9):]
    plt.figure(figsize=(10,6))
    plt.grid(True)
    plt.title(config["prepare_data"]["split_data"]["title"], fontsize = 14)
    plt.xlabel(config["prepare_data"]["split_data"]["xlabel"])
    plt.ylabel(config["prepare_data"]["split_data"]["ylabel"])
    plt.plot(df_log, 'green', label='Train data')
    plt.plot(test_data, 'blue', label='Test data')
    plt.legend()
    plt.savefig("train-test-series.png")
    
    return train_data, test_data