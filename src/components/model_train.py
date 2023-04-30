import os 
import sys
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from src.loging import logging
from src.exception import CustomException
from dataclasses import dataclass
from src.utils import evalute_model
from src.components.data_ingetion import DataIngetion
from src.components.data_transformation import DataTransformer
from src.utils import save_object

@dataclass
class ModelTrainConfig:
    model_train_file_path:str = os.path.join('artifacts', 'model.pkl')

class model_train :
    def __init__(self):
        self.model_train_config = ModelTrainConfig()

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
            #call to the utils file for the model evalution
            model_report:dict= evalute_model(X_train, y_train, X_test, y_test,models)
            logging.info("Done Model Trained")
           
            print(model_report)
            logging.info(f'Model Report : {model_report}')
            
            
            #Put the all the model with value one by one in the list
            list1 = []
            for model, values in model_report.items():
                list1.append([values[3],model,values])

            #take the highest value of the r2score 
            best_model = max(list1)
            best_model_name = models[best_model[1]]
            print("="*137)
            print("The Best Model is : ", best_model[1])
            print("Mean absolute error is :", best_model[2][0])
            print("Mean squared error is :", best_model[2][1])
            print("root Mean absolute error is :", best_model[2][2])
            print("R2_score is :", best_model[2][3])
            print("="*137)

            
            logging.info("Done Evalutionn of the model")
            save_object(
                 file_path=self.model_train_config.model_train_file_path,
                 obj=best_model_name
            )

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














