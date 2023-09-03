from MLProjects import logger
from MLProjects.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline




STAGE_NAME = "Data Ingestion stage"
try:

except Exception as e:
        logger.exception(e)
        raise e