import logging
import os 
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
os.makedirs("Log", exist_ok=True)
os.path.join("Log", LOG_FILE)

logging.basicConfig(filename = os.path.join("Log", LOG_FILE),format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",level=logging.INFO)
