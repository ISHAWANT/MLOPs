from src.logger.logging import logging 
from src.exception.exception import customexception  
from sklearn.model_selection import train_test_split

import pandas as pd 
import numpy as np 
import os
import sys 
from pathlib import Path  
from dataclasses import dataclass


@dataclass
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
            data = pd.read_csv("https://raw.githubusercontent.com/ISHAWANT/Data_set/main/Gemstone_Price_Prediction.csv")
            logging.info('reading a data frame') 
            os.makedirs(os.path.dirname(os.path.join(self.ingestion_config.raw_data_path)),exist_ok=True)
            data.to_csv(self.ingestion_config.raw_data_path,index=False)
            logging.info('Saved the raw dataset in artifact folder') 
            logging.info('Spliting the data into train and test') 

            train_data,test_data = train_test_split(data,test_size=0.25)
            logging.info("Train Test spliting completed") 

            train_data.to_csv(self.ingestion_config.train_data_path,index=False)
            test_data.to_csv(self.ingestion_config.test_data_path,index=False)

            logging.info('Data ingestion part completed')

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            # logging.info()
            raise customexception(e,sys)

if __name__=='__main__':
    obj = DataIngestion() 
    obj.initiate_data_ingestion() 

