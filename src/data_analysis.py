"""

The script obtains various visualizations of the cleaned dataset 
& stores them in "visualization" directory

"""
import os

from utility import create_log, parse_config, read_data
from data_analysis_util import plot_prices, plot_density

create_log("data_analysis.log")  # Creating log file

##################################################
#-----------------Reading Dataset-----------------
##################################################

config_path = "../config/config.yaml"   
config = parse_config(config_path)   # read config file
data_path = config["data_analysis"]["data"]   # read dataset
df_clean = read_data(data_path)
os.chdir('../visualizations')  # directory to save visualization figures


#%% 
###################################################
# ---------------- Plot House Price  --------------
###################################################

plot_prices(df_clean, "Date", "all_homes")

#%% 
###################################################
# ---------------- Price Density  -----------------
###################################################

plot_density(df_clean)

os.chdir('../src')  # resetting to src path 