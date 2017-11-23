#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Home assignment [PT2-06-17][P11]"""

import threading
import time
import sys
import logging
import os
from mmap import mmap

logger = logging.getLogger(__name__)
logfile = "script_log.log"
span_time = 2
run_tracker = []

formatter = logging.Formatter('%(asctime)s - %(name)s : %(threadName)s - %(levelname)s - %(message)s')
screen_handler = logging.StreamHandler(sys.stdout)
screen_handler.setLevel(logging.DEBUG)
screen_handler.setFormatter(formatter)

file_handler = logging.FileHandler(logfile)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

logger.addHandler(screen_handler)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

start_time = time.time()


def threaded_execution(*args, **kwargs):
    """Decorator of the main functionality"""
    # TODO: here be your code that runs a decorated function in a separate thread
    # MODIFY-START
    def wrapped(filename):
        """Wrapper function"""
        thread = threading.Thread(target=args[0], args=(filename,))
        thread.start()

    return wrapped
    # MODIFY-END


@threaded_execution
def long_long_function(filename):
    """Decorated function"""
    logger.info("Filename to work with: {}".format(filename))
    run_tracker.append(filename)
    time.sleep(span_time)
    # TODO: here be your code that works on file content:
    # MODIFY-START
    mod_filename = 'truncated_' + filename
    with open(filename, 'r+') as first_file, open(mod_filename, 'w+') as second_file:
        dev_file = mmap(first_file.fileno(), os.path.getsize(first_file.name))
        nl_count = 0
        quantity_to_read = 10
        i = dev_file.size() - 1
        if dev_file[i] == '\n':
            quantity_to_read += 1
        while nl_count < quantity_to_read and i > 0:
            if dev_file[i] == '\n':
                nl_count += 1
            i -= 1
        if i > 0:
            i += 2
        for element in dev_file[i:].splitlines():
            second_file.write(element + '\n')
            # MODIFY-END


if __name__ == "__main__":
    logger.info("Starting a chain of long functions")
    long_long_function("input_file1.txt")
    long_long_function("input_file2.txt")

    logger.info("Starting long main logic")
    time.sleep(span_time)

    ########################
    # --- Summary part --- #
    ########################
    total_time = time.time() - start_time
    logger.info("The run took '{:.3}' seconds".format(total_time))
    assert len(run_tracker)  # Do NOT remove or change, we need to ensure long_long_function ever ran
    assert total_time < (span_time + 1)  # +1 second is granted for all the threads to get allocated
