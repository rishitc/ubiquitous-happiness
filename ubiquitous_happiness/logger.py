import logging
import os


BASE_METADATA_PATH = os.path.join("ubiquitous_happiness", "metadata")

LOG_COUNT_FILE = os.path.join(BASE_METADATA_PATH, ".log_count.txt")
LOG_COUNT_FILE = os.path.abspath(LOG_COUNT_FILE)
print(os.getcwd())

# If the file to hold the number of logs captured does not exist then
# create one.
if not os.path.isfile(LOG_COUNT_FILE):
    with open(LOG_COUNT_FILE, "w") as file_handler:
        file_handler.write("1")
    count = 0

else:  # If the log counts file exits
    # Read in the the current log count
    with open(LOG_COUNT_FILE, "r") as file_handler:
        count = int(file_handler.readline())

    # Empty the file and store the new count value in the file for
    # the next time the program is run and logs need to be generated
    with open(LOG_COUNT_FILE, "w") as file_handler:
        temp = count + 1
        file_handler.write(str(temp))

logging.basicConfig(filename=os.path.join(BASE_METADATA_PATH, "logs",
                                          f"log_{count}.log"),
                    format=("%(asctime)s : %(name)s : %(levelname)s :"
                            " %(message)s"),
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)
