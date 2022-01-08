"""

The script determines ARIMA parameters; and trains ARIMA; on train set. 
Using the model; forecast is obtained for the test set.   

The results suitably plotted and evaluated. 

"""

import os
import pandas as pd
from logzero import logger, logfile
import pickle

from model_data_util import diagnose_arima
from statsmodels.tsa.arima_model import ARIMA

import matplotlib.pyplot as plt

from utility import create_log, parse_config, read_data

create_log("model_data.log")  # Creating log file


os.chdir("../visualizations")

# %%
##################################################
#-------------Reading Dataset & Config------------
##################################################
config_path = "../config/config.yaml"   
config = parse_config(config_path)   # read config file

train_data = read_data(config["model_data"]["train_data"])

test_data = read_data(config["model_data"]["test_data"])

# %%
#####################################################
#-------------------Diagnose Arima-------------------
#####################################################

diagnose_arima(train_data)


# %%
#####################################################
#----------------Build & Train Model-----------------
#####################################################

model = ARIMA(train_data, order=(0,1,2))  
fitted = model.fit(disp=-1)  
print(fitted.summary())



# %%
#####################################################
#---------------------Forecast Prices----------------
#####################################################
# Forecast
fc, se, conf = fitted.forecast(len(test_data), alpha=0.05)  # 95% conf


plt.style.use('fivethirtyeight')

# Make as pandas series
fc_series = pd.Series(fc, index=test_data.index)
lower_series = pd.Series(conf[:, 0], index=test_data.index)
upper_series = pd.Series(conf[:, 1], index=test_data.index)

# Plot
plt.figure(figsize=(10,7), dpi=100)
plt.plot(train_data, label='training data')
plt.plot(test_data, color = 'blue', label='Actual Stock Price')
plt.plot(fc_series, color = 'orange',label='Predicted Stock Price')
plt.fill_between(lower_series.index, lower_series, upper_series, 
                 color='k', alpha=.10)
plt.title('House Price Forecast of Alabama')
plt.xlabel('Years')
plt.ylabel('House Price')
plt.legend(loc='upper left', fontsize=8)
plt.savefig("price_forecast.png")

    
# %%
# Saving Model
file = open('../model/model.pkl', 'wb')   # Open a file to store model
pickle.dump(fitted, file)   # dumping information to the file
file.close()
