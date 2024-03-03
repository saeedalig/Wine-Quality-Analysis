from WineQualityAnalysis.config.configuration import ConfigurationManager
from WineQualityAnalysis.components.model_evaluation import ModelEvaluation
from WineQualityAnalysis import logger
from pathlib import Path


STAGE_NAME = "Model evaluation Stage"


class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation_config = ModelEvaluation(config=model_evaluation_config)
        model_evaluation_config.save_results()



if __name__ == '__main__':
    try:
        logger.info(f">>>>>>  {STAGE_NAME}: Started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>  {STAGE_NAME}: Completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e