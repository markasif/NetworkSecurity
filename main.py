from networksecurity.components.data_injestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig
import sys

if __name__ =="__main__":
    try:
         trainingpipelineconfig = TrainingPipelineConfig()
         dataingestionconfig = DataIngestionConfig( trainingpipelineconfig)
         data_ingestion =DataIngestion(dataingestionconfig)
         logging.info("Initate the data ingestion")
         dataingestionartifacts=data_ingestion.initiate_data_ingestion()
         print(dataingestionartifacts)
    except Exception as e:
        raise NetworkSecurityException(e,sys)
