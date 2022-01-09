"""

The script declares the functions used in 'model_data.py'

"""
from logzero import logger

import matplotlib.pyplot as plt

from pmdarima.arima import auto_arima

from utility import parse_config


##################################################
#-----------------Reading Config------------------
##################################################

config_path = "../config/config.yaml"   
config = parse_config(config_path)   # read config file

##################################################
#-----------------Declaring Functions-------------
##################################################

def diagnose_arima(train_data):
    model_autoARIMA = auto_arima(train_data, start_p=0, start_q=0,
                          test='adf',       # use adftest to find optimal 'd'
                          max_p=3, max_q=3, # maximum p and q
                          m=1,              # frequency of series
                          d=None,           # let model determine 'd'
                          seasonal=False,   # No Seasonality
                          start_P=0, 
                          D=0, 
                          trace=True,
                          error_action='ignore',  
                          suppress_warnings=True, 
                          stepwise=True)
    logger.info(model_autoARIMA.summary())
    
    model_autoARIMA.plot_diagnostics(figsize=(15,8))
    plt.suptitle(config["model_data"]["diagnose_arima"]["title"], fontsize = 18)
    plt.savefig("arima_diagnosis.png")
 
    
    