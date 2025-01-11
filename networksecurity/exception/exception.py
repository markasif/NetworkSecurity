import sys
from networksecurity.logging.logger import logging

class NetworkSecurityException(Exception):
    def __init__(self, error_message,error_details:sys):
        self.error_message = error_message
        _,_,exc_tb = error_details.exc_info()

        self.lineno = exc_tb.tb_lineno
        self.file_name = exc_tb.tb_frame.f_code.co_filename

    def __str__(self):
        return "Error Occur in Python  Script Name [{0}] line number [{1}] error message [{2}]".format(
        self.file_name,self.lineno,str(self.error_message))
if __name__ =="__main__":
    try:
        a=1/0
        logging.info("Entered the try block")
        print("this will not be printed")
    except Exception as e:
        raise NetworkSecurityException(e,sys)
