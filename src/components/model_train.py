import os 
import sys
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from src.loging import logging
from src.exception import CustomException
from dataclasses import dataclass
from src.utils import evalute_model
from src.components.data_ingetion import DataIngetion
from src.components.data_transformation import DataTransformer


@dataclass
class ModelTrainConfig:
    model_train_file_path:str = os.path.join('artifacts', 'model.pkl')

class model_train :
    def __init__(self):
        self.model_train_confing = ModelTrainConfig()

    def intate_model_train(self,train_arr, test_arr):
        try :
            logging.info("Initiate the model_training")
            #Now create the X_train, X_test, y_train, y_test of the data 
            X_train, y_train, X_test, y_test = (
                train_arr[ : , : -1],
                train_arr[ : , -1],
                test_arr[ : , : -1],
                test_arr[ : , -1],
            )

            #Now model training perform on the data 
            models={
                'LinearRegression':LinearRegression(),
                'Lasso':Lasso(),
                'Ridge':Ridge(),
                'Elasticnet':ElasticNet()
            }

            #Now model Evalute the from the by the method in the util
            logging.info("Start the model evalution")
            model_report:dict= evalute_model(X_train, y_train, X_test, y_test,models)
            logging.info("Done Model Trained")
           
            print(model_report)
            logging.info(f'Model Report : {model_report}')
            
            
            
            list1 = []
            for model, values in model_report.items():
                list1.append([values[3],model,values])

            best_model = max(list1)
            print("="*137)
            print("The Best Model is : ", best_model[1])
            print("Mean absolute error is :", best_model[2][0])
            print("Mean squared error is :", best_model[2][1])
            print("root Mean absolute error is :", best_model[2][2])
            print("R2_score is :", best_model[2][3])
            print("="*137)

            
            logging.info("Done Evalutionn of the model")

        except Exception as e :
            logging.info("Error is occured in the model_trainer")
            raise CustomException(e,sys)

if __name__ =="__main__"  :   
    o = DataIngetion()
    train_data_path, test_data_path = o.data_ingetion_intiate()
    object_data_transformation = DataTransformer()
    train_arr, test_arr, _ = object_data_transformation.intiate_data_transformation(train_data_path, test_data_path)
    object_model_train = model_train()
    object_model_train.intate_model_train(train_arr, test_arr)

        #













