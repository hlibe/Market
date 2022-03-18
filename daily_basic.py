#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 21:12:38 2021

@author: HaoLI
"""
import os
import pandas as pd
import tushare as ts
import datetime


os.getcwd()
# set global directory
PP = '/Users/HaoLI/Market'
os.chdir(PP)
#get today's date YYYYmmdd
today = datetime.date.today().strftime("%Y%m%d")
# token from tushare
ts.set_token('feddebfa68286f38ad93ec39a1ca0c58c085c7c0457ab29df627f028')

stocknumber1 = '600158.SH'

pro = ts.pro_api()

df = pro.daily_basic(ts_code=stocknumber1, trade_date='20180726', fields='ts_code,trade_date,turnover_rate,volume_ratio,pe,pb')
