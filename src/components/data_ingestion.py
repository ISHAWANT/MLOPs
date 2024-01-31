from src.logger.logging import logging 
from src.exception.exception import customexception  
from sklearn.model_selection import train_test_split

import pandas as pd 
import numpy as np 
import os
import sys 
from pathlib import Path  
from dataclasses import dataclasse


@dataclasse
class DataIngestionConfig:
    raw_data_path:str = os.path.join("artifacts","raw.csv") 
    train_data_path:str = os.path.join("artifacts","train.csv") 
    test_data_path:str = os.path.join("artifacts","test.csv") 



class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig() 


    def initiate_data_ingestion(self):
        logging.info("Data ingestion started")
        try:
            data = pd.read_csv("ttps://raw.githubusercontent.com/ISHAWANT/Data_set/main/Gemstone_Price_Prediction.csv")
            logging.info('reading a data frame') 

            os.makedirs(os.path.join)
        except Exception as e:
            logging.info()
            raise customexception(e,sys)

