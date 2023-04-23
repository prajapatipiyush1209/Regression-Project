from src.loging import logging
from sklearn.metrics import mean_absolute_error, mean_squared_error,r2_score
import numpy as np
def evalute_model(X_train, y_train, X_test, y_test,models):
    report = {}
    for i in range(len(models)):
        #Select the model 
        model = list(models.values())[i]

        #train the model means that analysis the pattern in the data between the X_train data and y_train data 
        model.fit(X_train,y_train)
    
        #Now predict the for the X_test from the training data 
        
        y_pred = model.predict(X_test)

        mae = mean_absolute_error(y_pred, y_test)
        mse = mean_squared_error(y_pred, y_test)
        rmse = np.sqrt(mean_squared_error(y_pred, y_test))
        r2_square = r2_score(y_pred, y_test)*100

        report[list(models.keys())[i]] = [mae,mse,rmse,r2_square]
        
    return report



