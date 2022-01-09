"""

The script develops an application form to read user's region,
and accordingly forecasts housing prices 

"""

import pandas as pd
import streamlit as st
import numpy as np

import matplotlib.pyplot as plt

from datetime import timedelta
from statsmodels.tsa.arima_model import ARIMA


#%%
############################################################
#--------------------- Application Form--------------------- 
############################################################

st.title('House Price Forecasting Application')
st.write("Identify the regions; that offer largest property rise.")
st.write("HAPPY INVESTING !!")
st.write("")


st.markdown('Select Region')

region_names = ['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado',
       'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
       'Illinois', 'Indiana', 'Iowa', 'Kentucky', 
       'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
       'Mississippi', 'Missouri', 'Nebraska', 'Nevada', 'NewHampshire',
       'NewJersey', 'NewMexico', 'NorthCarolina', 'Ohio',
       'Oklahoma', 'Oregon', 'Pennsylvania', 'RhodeIsland',
       'SouthCarolina', 'Tennessee', 'Texas', 'Utah', 'Virginia',
       'Washington', 'WestVirginia']    # NewYork, Kansas, Louisiana is corrupted



selected_region = st.selectbox("", region_names)

st.subheader("")
st.markdown("How many years you want to forecast?")


selected_years = st.slider('', min_value = 1, 
                            max_value = 20, step = 1, 
                            value = 6)

#%%
################################################################
# -------------------- Reading Data & Model --------------------
################################################################

def read_data(data_path):

    try:
        date_parse = lambda dates: pd.datetime.strptime(dates, '%Y-%m-%d')
        
        
        df = pd.read_csv(data_path, index_col = "Date", parse_dates = ["Date"], date_parser = date_parse)
        print('Dataset with {} and {} features was loaded successfully.'.format(*df.shape))  # Writing to logfile
        return df
    
    except:
        print('Dataset was not loaded. Please ensure that dataset is provided and is named correctly.')

df = read_data('../data/regions/{}.csv'.format(selected_region)) 
df_close = df.iloc[:, 0]

##########################################################
#---------------- Extracting forecast days----------------
##########################################################

df_1 = pd.DataFrame()

df_1["Date"] = pd.to_datetime(df.index)

ref_date = df_1.iloc[-1, 0]

end_date = (ref_date + timedelta(days=300*selected_years)).isoformat()

fc_days = pd.date_range(start =ref_date, end = end_date, freq ='1M')

fx = pd.DataFrame()

fx[0] = fc_days 


#%%
#######################################################
#--------------------- Remove Trend--------------------
#######################################################

def remove_trend(df):

#    rcParams['figure.figsize'] = 10, 6
    df_log = np.log(df)
    moving_avg = df_log.rolling(12).mean()
    std_dev = df_log.rolling(12).std()
    plt.legend(loc='best')
    plt.title('Moving Average')
    plt.plot(std_dev, color ="black", label = "Standard Deviation")
    plt.plot(moving_avg, color="red", label = "Mean")
    plt.legend()
    plt.show()
    return df_log

df_log = remove_trend(df_close)


# %%
#################################################
# ------------- Build & Train Model ------------- 
#################################################

model = ARIMA(df_log, order=(1,1,2))  
fitted = model.fit(disp=-1)  # ()  

#%%
################################################
# ------------- Forecasting Prices -------------
################################################
df_log = np.exp(df_log)
fc, se, conf = fitted.forecast(len(fx), alpha=0.05)  # ------27 removed------ 95% conf
plt.style.use('fivethirtyeight')

# Make as pandas series
fc_series = pd.Series(fc, index = fx[0])
lower_series = pd.Series(conf[:, 0], index = fx[0])
upper_series = pd.Series(conf[:, 1], index = fx[0])


fc_series = np.exp(fc_series)
lower_series = np.exp(lower_series)
upper_series = np.exp(upper_series)

# Plot
fig = plt.figure(figsize=(10,7), dpi=100)
plt.plot(df_close, color = 'blue', label='Actual Stock Price')
plt.plot(fc_series, color = 'orange',label='Predicted Stock Price')
plt.fill_between(lower_series.index, lower_series, upper_series, 
                 color='k', alpha=.10)
plt.title('House Price Forecast of {}'.format(selected_region))
plt.xlabel('Years')
plt.ylabel('House Prices')
plt.legend(loc='upper left', fontsize = 10)
st.write(fig)