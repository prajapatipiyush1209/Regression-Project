import sys 
import pandas as pd 
import numpy as np 
from sklearn.impute import SimpleImputer 
from sklearn.preprocessing import OrdinalEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from dataclasses import dataclass
import os
from src.loging import logging
from src.exception import CustomException

#create data transformerconfig
@dataclass
class DataTransformerConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'processor.pkl')

#intiate the DataTransormer 
class DataTransformer:
    def __init__(self):
        self.data_transformation_config= DataTransformerConfig()
    
    def get_transforation_object(self):
        try :
            logging.info("Data Transformation is intiate")
            # Diffrentiate the categorical and numerical columns
            categorical_cols = ['cut', 'color','clarity']
            numerical_cols = ['carat', 'depth','table', 'x', 'y', 'z']

            ##Ranking of the categorical data for the Encoding
            cut_categories = ['Fair', 'Good', 'Very Good','Premium','Ideal']
            color_categories = ['D', 'E', 'F', 'G', 'H', 'I', 'J']
            clarity_categories = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']
            
            logging.info("Pipeline creating")
            #Pipeline create 
            num_pipeline = Pipeline(
                steps =[
                ('imputer',SimpleImputer(strategy='median')), 
                ('scaler',StandardScaler())
                ]
                )
            cat_pipeline = Pipeline(
                steps=[
                ('imputer',SimpleImputer(strategy='most_frequent')),
                ('ordinalencoder',OrdinalEncoder(categories=[cut_categories,color_categories,clarity_categories])),
                ('scaler',StandardScaler())
                ]
                )
            preprocessor=ColumnTransformer([
            ('num_pipeline',num_pipeline,numerical_cols),
            ('cat_pipeline',cat_pipeline,categorical_cols)
            ])

            logging.info("Done Pipelineing")
            return preprocessor
        
        except Exception as e :
            logging.info("Error is occuring")
            raise CustomException(e,sys)
        
    def intiate_data_transformation(self,train_data_path, test_data_path):
            try :
                
                #reading data from the file 
                train_df = pd.read_csv(train_data_path)
                test_df = pd.read_csv(test_data_path)
                
                
                logging.info('Read train and test data completed')
                logging.info(f'Train Dataframe Head : \n{train_df.head().to_string()}')
                logging.info(f'Test Dataframe Head  : \n{test_df.head().to_string()}')

                #Now divide the data into the X_train, X_test and y_train, y_test 
                X_train = train_df.drop(labels=['id','price'], axis = 1)
                X_test = test_df.drop(labels=['id', 'price'], axis=1)
                  
                y_train = train_df['price']
                y_test = test_df['price']
                logging.info(X_train.shape)
                logging.info(X_test.shape)
                logging.info("Created X_tRAIN, X_test, y_train, y_test data")

                
                logging.info("call the preprocessor object for performing the fit_transform method")
                preprocessor = self.get_transforation_object()
                #Now transforming the using preprocessor object
                X_train = preprocessor.fit_transform(X_train)
                X_test = preprocessor.transform(X_test)
                logging.info("Applying preprocessing object on training and testing datasets.")
                
                
                train_arr = np.c_[X_train, np.array(y_train)]
                test_arr = np.c_[X_test, np.array(y_test)]

                return (train_arr, test_arr,self.data_transformation_config.preprocessor_obj_file_path)
            
            except Exception as e :
                logging.info("Error is occured in the intiate_transformation")
                raise CustomException(e,sys)