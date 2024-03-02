


from WineQualityAnalysis import logger
from WineQualityAnalysis.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from WineQualityAnalysis.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
# from WineQualityAnalysis.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
# from WineQualityAnalysis.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
# from WineQualityAnalysis.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>>>>>>>>  {STAGE_NAME}: Started <<<<<<<<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>>>>> {STAGE_NAME}: Completed <<<<<<<<<<<<<<\n\nx===================x")
except Exception as e:
    raise e


STAGE_NAME = "Data Validation Stage"
try:
   logger.info(f">>>>>>  {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataValidationTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>>  {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
        logger.exception(e)
        raise e