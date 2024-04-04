import logging
import sys
import os
from dependecy.file_config import create_file

create_file()

file_directory = "data-log"
new_file = "log.txt"
file_path = os.path.join(file_directory, new_file)



logger = logging.getLogger()


formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s")


stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler(file_path)

stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.handlers = [stream_handler, file_handler]


logger.setLevel(logging.INFO)