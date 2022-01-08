
"""

The script converts checks stationarity, 
accordingly removes the trend and 
splits train and test sets

"""

#import pandas as pd
#from logzero import logger, logfile
import os
import pathlib
from utility import create_log, parse_config, read_data
from prepare_data_util import stationarity_test, decompose_series, remove_trend, split_data

create_log("prepare_data.log")  # Creating log file

os.chdir("../visualizations")

# %%
##################################################
#-----------------Reading Dataset-----------------
##################################################
config_path = "../config/config.yaml"   
config = parse_config(config_path)   # read config file
data_path = config["prepare_data"]["data"]   # read dataset
df_clean = read_data(data_path)


# %%
#####################################################
#------------------Check Stationarity----------------
#####################################################

stationarity_test(df_clean)


# %%
#####################################################
#----------------Decompose Time-Series---------------
#####################################################

decompose_series(df_clean)


# %%
#####################################################
#------------Removing Trend from Series--------------
#####################################################
#if not stationary then eliminate trend
#Eliminate trend

df_log = remove_trend(df_clean)



# %%
#####################################################
#---------------------Split Data---------------------
#####################################################

train_data, test_data = split_data(df_log)


# Saving train and test sets 
tgt_path = pathlib.Path.cwd().parent.joinpath('data/train_data.csv')  # declaring file path
train_data.to_csv(tgt_path, index = True)   # saving file

tgt_path = pathlib.Path.cwd().parent.joinpath('data/test_data.csv')  # declaring file path
test_data.to_csv(tgt_path, index = True)   # saving file


# %%
# resetting directory
os.chdir("../src")


