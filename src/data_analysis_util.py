"""

The script declares functions used in 'data_analysis.py'

"""

import matplotlib.pyplot as plt
from utility import parse_config

config_path = "../config/config.yaml"   
config = parse_config(config_path)   # read config file


def plot_prices(df, date_col, price_col):
    plt.figure(figsize=(10,6))
    plt.grid(True)
    plt.xlabel(config["data_analysis"]["plot_prices"]["xlabel"])
    plt.ylabel(config["data_analysis"]["plot_prices"]["ylabel"])
    plt.plot(df[price_col])
    plt.title(config["data_analysis"]["plot_prices"]["title"])
    plt.savefig("house_prices.png")
    
    
def plot_density(df):
    fig, ax = plt.subplots()
    df.plot(kind='kde', ax=ax)
    ax.legend([config["data_analysis"]["plot_density"]['legend']])
    fig.savefig("price_density.png")
