from networksecurity.components.data_injestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
from networksecurity.components.data_validation import DataValidation,DataValidationConfig
import sys

if __name__ =="__main__":
    try:
         trainingpipelineconfig = TrainingPipelineConfig()
         dataingestionconfig = DataIngestionConfig( trainingpipelineconfig)
         data_ingestion =DataIngestion(dataingestionconfig)
         logging.info("Initate the data ingestion")
         dataingestionartifacts=data_ingestion.initiate_data_ingestion()
         print(dataingestionartifacts)
         logging.info("Data initiation completed")
         data_validation_config = DataValidationConfig(trainingpipelineconfig)
         data_validation =DataValidation(dataingestionartifacts,data_validation_config)
         logging.info("Initate the data validation")
         data_validation_Artifact=data_validation.initiate_data_validation()
         logging.info("data validation is completed")
         print(data_validation_Artifact)

    
    except Exception as e:
        raise NetworkSecurityException(e,sys)
