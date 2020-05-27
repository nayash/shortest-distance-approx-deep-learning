#
# Copyright (c) 2020. Asutosh Nayak (nayak.asutosh@ymail.com)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#


"""
Utility functions
"""
import re
import time
import numpy as np
import urllib.request
import shutil
import os
import pandas as pd
from matplotlib import pyplot as plt
import winsound
import time


def seconds_to_minutes(seconds):
    return str(seconds // 60) + " minutes " + str(np.round(seconds % 60)) + " seconds"


def print_time(text, stime):
    seconds = (time.time() - stime)
    print(text, seconds_to_minutes(seconds))


def get_readable_ctime():
    return time.strftime("%d-%m-%Y %H_%M_%S")


def download_save(url, path_to_save, logger=None):
    if logger:
        logger.append_log("Starting download " + re.sub(r'apikey=[A-Za-z0-9]+&', 'apikey=my_api_key&', url))
    else:
        print("Starting download " + re.sub(r'apikey=[A-Za-z0-9]+&', 'apikey=my_api_key&', url))
    urllib.request.urlretrieve(url, path_to_save)
    if logger:
        logger.append_log(path_to_save + " downloaded and saved")
    else:
        print(path_to_save + " downloaded and saved")


def remove_dir(path):
    shutil.rmtree(path)
    print(path, "deleted")
    # os.rmdir(path)


def dict_to_str(d):
    return str(d).replace("{", '').replace("}", '').replace("'", "").replace(' ', '')


def cleanup_file_path(path):
    return path.replace('\\', '/').replace(" ", "_").replace(':', '_')


def plot(y, title, output_path, x=None):
    fig = plt.figure(figsize=(10, 10))
    # x = x if x is not None else np.arange(len(y))
    plt.title(title)
    if x is not None:
        plt.plot(x, y, 'o-')
    else:
        plt.plot(y, 'o-')
        plt.savefig(output_path)


def sound_alert(repeat_count=5):
    duration = 1000  # millisecond
    freq = 440  # Hz
    for i in range(0, repeat_count):
        winsound.Beep(freq, duration)
        time.sleep(1)


def console_pretty_print_df(df):
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
        print(df)


def unison_shuffle_copies(a, b):
    assert len(a) == len(b)
    p = np.random.permutation(len(a))
    return a[p], b[p]
