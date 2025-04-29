import logging

logger = logging.getLogger("log_file_demo")

logger.setLevel(logging.INFO)
fh_stream = logging.StreamHandler()
fh_stream.setLevel(logging.INFO)