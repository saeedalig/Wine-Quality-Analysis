import os
import sys
import logging
from datetime import datetime 


log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

logging_str_format = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

logging.basicConfig(
    level = logging.INFO,
    format = logging_str_format,

    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger("WineQualityAnalysis")
