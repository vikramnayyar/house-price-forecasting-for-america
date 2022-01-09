
"""

The script reads and analyzes the dataset. After reading, it is oberved that
dataset cleaning is not required.

Also, the **region-wise** datasets are extecated and saved. This is 
required for the application to accept user inputs. 

"""

from logzero import logger
from utility import create_log, download_dataset, parse_config, read_data
from get_data_util import analyze_data

create_log("get_data.log")  # Creating log file

config_path = "../config/config.yaml"   
config = parse_config(config_path)   # read config file

# downloading dataset
logger.info("Downloading dataset")
file_id = config["get_data"]["download_id"]
download_dataset(file_id)    # downloads data from gdrive (File size is larger than git limit)
logger.info("Dataset downloaded successfully")



##################################################
#-------------------Reading Data------------------
##################################################

data_path = config["get_data"]["data"]   # read dataset
df = read_data(data_path)
        
region_names = ['Alabama', 'Arizona', 'Arkansas', 'California', 'Colorado',
       'Connecticut', 'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho',
       'Illinois', 'Indiana', 'Iowa', 'Kansas', 'Kentucky', 'Louisiana',
       'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
       'Mississippi', 'Missouri', 'Nebraska', 'Nevada', 'NewHampshire',
       'NewJersey', 'NewMexico', 'NewYork', 'NorthCarolina', 'Ohio',
       'Oklahoma', 'Oregon', 'Pennsylvania', 'RhodeIsland',
       'SouthCarolina', 'Tennessee', 'Utah', 'Virginia',
       'Washington', 'WestVirginia']

for name in region_names:
    df = read_data(data_path)     # del
    df = df[["RegionName", "ZHVI_AllHomes"]]   # filtering cols   # "ZHVI_2bedroom" removed
    df = df[df["RegionName"] == name]    # Filtering state
    df = df.drop(["RegionName"], axis =1)   # removing state col 
    df.rename(columns={"ZHVI_AllHomes":'all_homes'}, inplace=True)   # renaming cols 
    # df.head()
    
    
    analyze_data(df)   # Analyzing dataset
    
    
    # Saving cleaned data
   
    if name == "Alabama":
        df.to_csv('../data/clean_data.csv'.format(name), index = True)    # Saving the file in the path  	
        logger.info("Cleaned dataset for Alabama was saved successfully.\n\n\n ")  
    

    # Saving region-wise data

    df.to_csv('../data/regions/{}.csv'.format(name), index = True)    # Saving the file in the path
 
logger.info("Region-wise dataset was saved successfully.\n\n")
