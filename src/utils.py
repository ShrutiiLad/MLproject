#all the common functions will be written here which can be used in any module of the project

import os
import sys
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error
from src.exception import CustomException
import dill

def save_object(file_path, obj):    
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            dill.dump(obj, file_obj)
            
    except Exception as e:
        raise CustomException(e, sys)