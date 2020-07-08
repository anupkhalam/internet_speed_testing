#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 18:08:38 2020.

@author: anup
"""

import speedtest
import datetime
import argparse
import pandas as pd
from apscheduler.schedulers.blocking import BlockingScheduler


def get_internet_speed(args_):
    """Get internet speed."""
    dt = datetime.datetime.now()
    details = {}
    details['Time'] = [dt.strftime("%X")]
    details['Day'] = [dt.strftime("%A")]
    details['Date'] = [dt.strftime("%d-%B-%Y")]
    s = speedtest.Speedtest()
    s.get_best_server()
    s.download(threads=None)
    s.upload(threads=None)
    results_dict = s.results.dict()
    details['Download speed (Mbps)'] = [round(results_dict['download'] /
                                              (1024*1024), 2)]
    details['Upload speed (Mbps)'] = [round(results_dict['download'] /
                                            (1024*1024), 2)]
    df_columns = ['Date',
                  'Day',
                  'Time',
                  'Download speed (Mbps)',
                  'Upload speed (Mbps)']
    try:
        dataset = pd.read_csv('data/consolidated.csv')
    except FileNotFoundError:
        dataset = pd.DataFrame(columns=df_columns)
    df1 = pd.DataFrame(details, columns=df_columns)
    dataset = dataset.append(df1, ignore_index=True)
    dataset.to_csv('data/consolidated.csv', index=None)

    if len(dataset) >= args['records']:
        df2 = dataset.tail(args['records'])
        avg_download_speed = dataset['Download speed (Mbps)'].mean()
        avg_upload_speed = dataset['Upload speed (Mbps)'].mean()
        if avg_download_speed < float(args['speed']) and \
           avg_upload_speed < float(args['speed']):
            df2.to_excel('data/speed_report.xlsx', index=None)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--speed", required=True,
                    help="Expected internet speed")
    ap.add_argument("-i", "--interval", required=True,
                    help="Interval in minutes")
    ap.add_argument("-i", "--records", required=True,
                    help="Number of records to capture in the report")
    args = vars(ap.parse_args())
    scheduler = BlockingScheduler()
    scheduler.add_job(func=get_internet_speed,
                      trigger='interval',
                      args=[args],
                      minutes=int(args['interval']))
    scheduler.start()
