import os 
import sys
from sklearn.model_selection import train_test_split
from src.exception import CustomException
from src.loging import logging
from dataclasses import dataclass
import pandas as pd
from src.components.data_transformation import DataTransformer
## Intitialize the Data Ingetion Configuration

@dataclass
class DataIngetionConfig:
    raw_data_path:str = os.path.join('artifacts','raw_data.csv')
    train_data_path:str = os.path.join('artifacts','train_data.csv')
    test_data_path:str= os.path.join('artifacts', 'test_data.csv')
    '''
    artifacts : In a machine learning project, the artifacts folder typically refers to a directory where the project outputs are stored. This can include trained machine learning models, data preprocessing scripts, documentation, and other project artifacts. The artifacts folder serves as a central location for all of the important project outputs, and helps to ensure that they are organized and easily accessible. By storing project artifacts in a dedicated folder, it also makes it easier to share the project with others, such as team members, stakeholders, or collaborators.
    '''

class DataIngetion :
    
    try :
        def __init__(self):
            self.data_ingetion_config = DataIngetionConfig() # Create the object of the class

        def data_ingetion_intiate(self):
            logging.info("Start data Ingetion")

            #Read the dta from the csv
            data = pd.read_csv(os.path.join('notebooks/Data', 'gemstone.csv'))
            #it's create the directory by using of the raw_data_path
            os.makedirs(os.path.dirname(self.data_ingetion_config.raw_data_path),exist_ok=True)

            #Noe save the data to path that point by the raw_data_pat
            data.to_csv(self.data_ingetion_config.raw_data_path, index=False)
            logging.info("Complete store the raw data")
            

            #Now Store the train and test data by using the train_test-split() method 
            train_data, test_data = train_test_split(data, test_size=0.30,random_state=42)
            logging.info("Train split completed")

            #Now store the test and train data into the artifacts folder 
            train_data.to_csv(self.data_ingetion_config.train_data_path)
            test_data.to_csv(self.data_ingetion_config.test_data_path)
            logging.info("complete the Data Ingetion")

            return (self.data_ingetion_config.train_data_path,self.data_ingetion_config.test_data_path)
    
    #If any exception is occured then handle 
    except Exception as e :
        logging.info("Error is occuring")
        raise CustomException(e,sys)
