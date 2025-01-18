import os
import sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.components.data_injestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer

from networksecurity.entity.config_entity import(
    TrainingPipelineConfig,
    DataIngestionConfig,
    DataValidationConfig,
    DataTransformationConfig,
    ModelTrianerConfig,
)

from networksecurity.entity.artifact_entity import(
    DataIngestionArtifact,
    DataTransformationArtifact,
    DataValidationArtifact,
    ModelTrainerArtifact,
)
import sys

class TrainingPipeline:
    def __init__(self):
        self.training_pipeline_config = TrainingPipelineConfig()

    def start_data_ingestion(self):
        try:
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info("start data ingestion")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"Data ingestion is completed and artifact is : {data_ingestion_artifact}")
            return data_ingestion_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_data_validation(self,data_ingestion_artifact : DataIngestionArtifact):
        try:
            data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            data_validation =DataValidation(data_ingestion_artifact=data_ingestion_artifact,data_validation_config=data_validation_config)
            logging.info("initate the data validation")
            data_validation_artifact = data_validation.initiate_data_validation()
            logging.info(f"Data valiation is ci=ompleted and artifact is : {data_validation_artifact}")
            return data_validation_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_data_transformation(self,data_validation_artifact : DataTransformationArtifact):
        try:
            data_transformation_config = DataTransformationConfig(training_pipeline_config=self.training_pipeline_config)
            data_transformation = DataTransformation(data_validation_artifact=data_validation_artifact,
                                                     data_transformation_config=data_transformation_config)
            logging.info("initate the data transformation")
            data_transformation_artifact = data_transformation.initiate_data_transformation()
            logging.info(f"Data transformation is completed and artifact is : {data_transformation_artifact}")
            return data_transformation_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def start_model_trainer(self,data_transformation_artifact : DataTransformationArtifact) -> ModelTrainerArtifact:
        try:
            self.model_trainer_config : ModelTrianerConfig = ModelTrianerConfig(
                training_pipeline_config=self.training_pipeline_config)
            
            model_trainer = ModelTrainer(
                data_transformation_artifact=data_transformation_artifact,
                model_trainer_config= self.model_trainer_config,
            )
            model_trainer_artifact = model_trainer.initiate_model_trainer()
            return model_trainer_artifact
        except Exception as e:
            raise NetworkSecurityException(e,sys)
        
    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact = self.start_data_transformation(data_validation_artifact=data_validation_artifact)
            data_model_artifact = self.start_model_trainer(data_transformation_artifact=data_transformation_artifact)
            return data_model_artifact
        except Exception as e:
            NetworkSecurityException(e,sys)