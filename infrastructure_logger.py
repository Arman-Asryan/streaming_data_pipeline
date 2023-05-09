import os
import logging
from configs import log_folder, infrstr_log_file


logging.basicConfig(
    level=logging.INFO,
    filename=os.path.join(log_folder, infrstr_log_file),
    format="%(asctime)s - %(levelname)s - %(message)s",
)