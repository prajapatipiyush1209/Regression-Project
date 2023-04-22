import sys 
from src.loging import logging



def error_msg_details(error,error_msg_detail:sys):#return the Error msg with line anf file name 
    _,_,exc_tb=error_msg_detail.exc_info() # exc_inf() of the sys class that return the Traceback 
    file_name = exc_tb.tb_frame.f_code.co_filename #getting the file name
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))
    return error_message

class CustomException(Exception):#Inherit the Exception class
    def __init__(self, error_msg, error_msg_detail:sys):#Constructor of the CustomExceptionn Class
        super().__init__(error_msg)# Call the method of the parent class
        self.error_msg = error_msg_details(error_msg, error_msg_detail=error_msg_detail) #call the method


    def __str__(self):
        return self.error_msg

logging.info('Start Exceution of the code')

'''
try :
    a=8
    b=8/0
except Exception as e:
    logging.info('Error Is occured')
    #Here Call to the Custom Exception class by using raise keyword
    raise CustomException(e,sys)
    '''