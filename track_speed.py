#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 18:08:38 2020.

@author: anup
"""

import speedtest
import glob
import datetime
import pandas as pd

files_list = glob.glob('data/*')
num_files = len(files_list)
new_file_name = "set_" + str(num_files)
dt = datetime.datetime.now()
details = {}
details['Time'] = dt.strftime("%X")
details['Month'] = dt.strftime("%B")
details['Day'] = dt.strftime("%A")
details['Date'] = dt.strftime("%d-%B-%Y")
threads = None
s = speedtest.Speedtest()
s.get_best_server()
s.download(threads=None)
s.upload(threads=None)
s.results.share()
results_dict = s.results.dict()
details['Download speed (Mbps)'] = round(results_dict['download']/(1024*1024),
                                         2)
details['Upload speed (Mbps)'] = round(results_dict['download']/(1024*1024),
                                       2)
if num_files > 0:
    dataset = pd.read_csv('set_' + str(num_files))
else:
    dataset = pd.DataFrame(details)


