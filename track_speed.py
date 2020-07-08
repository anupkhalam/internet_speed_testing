#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 18:08:38 2020.

@author: anup
"""

import speedtest
import datetime
import pandas as pd
from apscheduler.schedulers.blocking import BlockingScheduler


def get_internet_speed():
    """Get internet speed."""
    print("*********************")
    dt = datetime.datetime.now()
    details = {}
    details['Time'] = [dt.strftime("%X")]
    details['Day'] = [dt.strftime("%A")]
    details['Date'] = [dt.strftime("%d-%B-%Y")]
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download(threads=None)
    s.upload(threads=None)
    s.results.share()
    results_dict = s.results.dict()
    details['Download speed (Mbps)'] = [round(results_dict['download'] /
                                              (1024*1024), 2)]
    details['Upload speed (Mbps)'] = [round(results_dict['download'] /
                                            (1024*1024), 2)]
    dataset = pd.read_csv('data/consolidated.csv')
    df1 = pd.DataFrame(details, columns=['Date',
                                         'Day',
                                         'Time',
                                         'Download speed (Mbps)',
                                         'Upload speed (Mbps)'])
    dataset = dataset.append(df1, ignore_index=True)
    dataset.to_csv('data/consolidated.csv', index=None)

    if len(dataset) > 24:
        df2 = dataset.tail(24)
        avg_download_speed = dataset['Download speed (Mbps)'].mean()
        avg_upload_speed = dataset['Upload speed (Mbps)'].mean()
        if avg_download_speed < 50. and avg_upload_speed < 50.:
            df2.to_excel('data/speed_report.xlsx', index=None)


scheduler = BlockingScheduler()
scheduler.add_job(get_internet_speed, 'interval', hours=1)
scheduler.start()
