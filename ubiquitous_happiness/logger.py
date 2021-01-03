import logging


logging.basicConfig(filename="pressure.log",
                    format='%(asctime)s : %(levelname)s : Pressure : %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.INFO)
