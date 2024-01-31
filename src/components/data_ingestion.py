from src.logger.logging import logging 
from src.exception.exception import customexception  

import pandas as pd 
import numpy as np 
import os
import sys 
from pathlib import Path 


class DataIngestionConfig:
    pass

class DataIngestion:
    def __init__(self):
        pass

    def initiate_data_ingestion(self):
        try:
            pass
        except Exception as e:
            logging.info()
            raise customexception(e,sys)

