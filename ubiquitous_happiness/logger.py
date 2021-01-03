import logging
import os


LOG_COUNT_FILE = os.path.join(".", "metadata", ".log_count.txt")


# If the file to hold the number of logs captured does not exist then
# create one.
if not os.path.isfile(LOG_COUNT_FILE):
    with open(LOG_COUNT_FILE, "w") as file_handler:
        file_handler.write("1")
    count = 0
else:  # If the log counts file exits, then
    # Read in the the current log count
    with open(LOG_COUNT_FILE, "a") as file_handler:
        count = int(file_handler.readline())

    open('file.txt', 'w').close()  # Empty the file

    # Store the new count value in the file for the next time the
    # program is run, and the logs of the run are to be generated
    with open(LOG_COUNT_FILE, "a") as file_handler:
        temp = count + 1
        file_handler.write(str(temp))

logging.basicConfig(filename=os.path.join(".", "metadata", "logs"),
                    format=("%(asctime)s : %(name)s: %(levelname)s :"
                            " %(message)s"),
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)
