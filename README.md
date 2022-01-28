# House Price Forecasting for America

## Demo
The application is deployed in Heroku. The app is available in the link https://house-price-forecasting.herokuapp.com/.

## Introduction
An app is developed for forecasting house prices in America. App forecasts the prices for **40** American regions. The app was trained using <b>ARIMA</b> model and is developed in <b>Streamlit</b>. 

## Dataset
The dataset consists of actual house prices obtained from Zillow. It is a popular online real-estate and rental marketplace of America.

The dataset is avalailable in link: https://www.zillow.com/research/data/. It consists of **5 years** (monthly) house prices of <b>40</b> cities.

## Problem Statement
Numerous factors affect the rise of a property in a region. With the growth of real estate industry; many new regions have emerged. Therefore, there are several opportunities and manifold speculations and verdicts. Identifying a privileged property has become challenging.

Conventionally; customers tended to buy neaby properties. But, with globalisation and cultural convergence; customers are more open to newer locations. Presently, customers prefer premium property; that persistently develops. Property price reliably determines such development.

Therefore, such a project is vital for property sales.


## Goal



This work was performed as a personal project and is based on the dataset available on kaggle. The motivation was to obtain analysis of bank marketing campaign and identify customers the will make term deposits. For highest possible term deposits, a high accuracy was desirable for customer classification.   

An app classifying depositing customers, provides a very straightforward and intuitive means for identifying customers. This saves substantial <b>resources</b> and <b>time</b>. Also, this apporach is easily reproducible, thus; provides a <b>common</b> marketing platform to all the marketing teams and bank branches. The app will be utilized by the marketing team for accurate customer selection. Reduced errors in identifying customers will <b>increase</b> the bank deposits. 

## System Environment
![](https://forthebadge.com/images/badges/made-with-python.svg)



[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/e/ed/Pandas_logo.svg" width=200>](https://pandas.pydata.org/)     [<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/31/NumPy_logo_2020.svg/512px-NumPy_logo_2020.svg.png" width=200>](https://numpy.org/)     



[<img target="_blank" src="https://www.metachris.com/images/posts/logzero/logo-text-wide-cropped.png" width=200>](https://pypi.org/project/logzero/)     [<img target="_blank" src="https://user-images.githubusercontent.com/965439/27257445-8791ea14-539c-11e7-8f5a-eec6cdfababa.png" width=200>](https://pypi.org/project/PyYAML/)     [<img target="_blank" src="https://phyblas.hinaboshi.com/rup/nayuki/2020/pythonsubprocess.png" width=200>](https://docs.python.org/3/library/subprocess.html)



[<img target="_blank" src="https://matplotlib.org/_static/logo2_compressed.svg" width=200>](https://matplotlib.org)     [<img target="_blank" src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" width=200>](https://seaborn.pydata.org/)             



[<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/0/05/Scikit_learn_logo_small.svg" width=200>](https://scikit-learn.org)     [<img target="_blank" src="https://www.h2o.ai/wp-content/uploads/2018/07/xgboost-narrow.png" width=200>](https://github.com/dmlc/xgboost)     [<img target="_blank" src="https://lightgbm.readthedocs.io/en/latest/_images/LightGBM_logo_black_text.svg" width=200>](https://lightgbm.readthedocs.io/en/latest/)     [<img target="_blank" src="https://landscape.lfai.foundation/logos/cat-boost.svg" width=200>](https://catboost.ai/)    


[<img target="_blank" src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png" width=200>](https://streamlit.io/)     [<img target="_blank" src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Heroku_logo.svg/2560px-Heroku_logo.svg.png" width=200>](https://www.heroku.com/)

## Technical Description
The main project scripts are in the **"src"** directory. Exceptionally, **"app.py"** is in app directory. The main constituting scripts are as follows

* **get_data.py:** The script reads the data from **bank.csv** file located in data directory. The dataset is analyzed, cleaned and saved as **"cleaned_data.csv"** in **data** directory. 

* **data_analysis.py:** This script obtains various visualizations of the dataset. These visualizations are saved in the **"Visualization"** directory. 

* **prepare_data.py:** The script converts the required features to **categorical** variables. Subsequent outliers are determined using Grubb's Test. These outliers are removed and cleaned dataset is saved as **"prepared_data.csv"**.   

* **split_data.py:** The cleaned dataset is split using stratified sampling. This ensures the fair splitting. The train and test sets are obtained after dataset splitting. Labels are separated from train and test sets and saved as **"train_labels.csv"** and **"test_labels.csv"**. Train data and test data are respectively saved as **"train_set.csv"** and **"test_set.csv"**.

* **model_data.py:** Various data science models are trained on train set. Accuracy of all the models is verified using test set. Henceforth, the best model is selected. The feature selection of the best model is optimized to increase the accuracy to **87.1 %** (approx). This model is saved as **"model.pkl"**. 

* **app.py:** The script develops a Streamlit app; that accepts 16 user inputs. These inputs are transformed and fed to **model.pkl**. The model's prediction is displayed in the application. 
 
* **run_project.py:** The script runs all the project scripts (discussed in this section) sequentially. Therefore, entire project is executed with this script.  

**get_data_util.py**, **data_analysis_util.py**, **prepare_data_util.py**, **split_data_util.py**, **model_data_util.py** and **utility.py** declare vital functions that are required by respective scripts. 

## Directory Structure

```bash
├── app                              # Application files
|  ├── app.py                        # Application script
├── config                           # Configuration files
|  ├── config.yaml                   # Configuration file  
├── data                             # Data files ()   
|  ├── bank.csv                      # Bank customer dataset 
|  ├── clean_data.csv                # Cleaned dataset 
|  ├── prepared_data.csv             # Prepared dataset 
|  ├── train_set.csv                 # Train data
|  ├── test_set.csv                  # Test data
|  ├── train_label.csv               # Train labels
|  ├── test_set.csv                  # Test labels
├── dict                             # Dictionary Files
|  ├── locations_dict.pkl            # Locations dictionary
|  ├── rest_type_dict.pkl            # Resaturant type dictionary
├── log                              # Log files
|  ├── get_data.log                  # "get_data.py" script logs
|  ├── data_analysis.log             # "data_analysis.py" script logs
|  ├── prepare_data.log              # "prepare_data.py" script logs 
|  ├── split_data.log                # "split_data.py" script logs 
|  ├── model_data.log                # "model_data.py" script logs 
├── model                            # Model Files
|  ├── model.pkl                     # Saved model
├── src                              # Main project scripts 
|  ├── get_data.log                  # Dataset acquistion and cleaning script
|  ├── data_analysis.log             # Dataset analysis and visualization script
|  ├── prepare_data.log              # Dataset preperation script
|  ├── split_data.log                # Dataset splitting script  
|  ├── model_data.log                # Dataset modelling script
├── visualizations                   # Dataset visualizations
|  ├── age_vs_deposit.png            # Age vs deposit figure
|  ├── bal_vs_deposit.png            # Balance vs deposit figure
|  ├── education_vs_deposit.png      # Education vs deposit figure
|  ├── job_vs_deposit.png            # Job vs deposit figure 
|  ├── marital_vs_deposit.png        # Marital vs deposit figure
|  ├── dataset_balance.png           # Dataset balance figure
|  ├── correlation_heatmap.png       # Correalation heatmap of features
|  ├── feature_importance.png        # Feature importance of best model
|  ├── cm_etc.png                    # Confusion matrix of ExtraTreesClassifier
|  ├── cm_gbc.png                    # Confusion matrix of GradientBoostClassifier
|  ├── cm_lgbm.png                   # Confusion matrix of LightGBMClassifier
|  ├── cm_rfc.png                    # Confusion matrix of RandomForestClassifier
|  ├── cm_xgb.png                    # Confusion matrix of XGBClassifier  
|  ├── cm_cbc.png                    # Confusion matrix of CatBoostClassifier
|  ├── cm_optimized_cbc.png          # Confusion matrix of optimized CatBoostClassifier
├── requirements.txt                 # Required libraries
├── Procfile                         # Required for Heroku deployment 
├── setup.sh                         # Required for Heroku deployment
├── LICENSE                          # License
├── README.md                        # Repository description

```

## Installing Dependencies
Foremost running the project, installing the dependencies is essential. 
* Ensure Python 3.8.8 or later is installed in the system. 
* All required libraries are listed in "requirements.txt". These are easily installed; by running the following command in project directory
```bash
pip install -r requirements.txt
```

## Run Project
As discussed in **Technical Aspect** section, "src" and “app” directory possess the main scripts. 

Running the following command in the "src" directory executes the entire project  
```bash
python3 run_project.py
```
Alternatively, a project script can be individually executed using the general script 
```bash
python3 script.py
```
Here “script.py” represents any python script. 

Exceptionally, application file "app.py" runs using command 
```bash
streamlit run app/app.py
```
**Note:** To run any project script, directory location must be correct.
