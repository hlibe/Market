#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 16:55:24 2022

@author: HaoLI
"""
import numpy as np
import pandas as pd
from futu import *

os.getcwd()
# set global directory
PP = '/Users/HaoLI/Market/data/capital_distribution'
os.chdir(PP)
'''
quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
ret, data = quote_ctx.get_plate_stock('HK.Motherboard') #获得所有主板股票代码
if ret == RET_OK:
    print(data)
    print(data['stock_name'][0])    # 取第一条的股票名称
    print(data['stock_name'].values.tolist())   # 转为 list
else:
    print('error:', data)
quote_ctx.close() # 结束后记得关闭当条连接，防止连接条数用尽
'''
stockcode = pd.Series(['HK.00700']) #将所有股票代码存入stockcode as series

#创造csv文档
for i in stockcode:
    if os.path.exists('%s.csv'%(i)): #如果该名称csv文件存在则读取
        pre_df = pd.read_csv('%s.csv'%(i))
        df = pre_df.loc[:, ['capital_in_big','capital_in_mid',
                    'capital_in_small','capital_out_big',
                    'capital_out_mid','capital_out_small',
                    'update_time']]
        quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
        ret, data = quote_ctx.get_capital_distribution(i)
        if ret == RET_OK:
            print(data)
            print(data['capital_in_big'][0])    # 取第一条的流入资金额度，大单
            print(data['capital_in_big'].values.tolist())   # 转为 list
        else:
            print('error:', data)
        quote_ctx.close() # 结束后记得关闭当条连接，防止连接条数用尽
        pieces = [df, data]
        new_df = pd.concat(pieces)
        new_df.to_csv('%s.csv'%(i))
    else:
        quote_ctx = OpenQuoteContext(host='127.0.0.1', port=11111)
        ret, data = quote_ctx.get_capital_distribution(i)
        if ret == RET_OK:
            print(data)
            print(data['capital_in_big'][0])    # 取第一条的流入资金额度，大单
            print(data['capital_in_big'].values.tolist())   # 转为 list
        else:
            print('error:', data)
        quote_ctx.close() # 结束后记得关闭当条连接，防止连接条数用尽
        data.to_csv('%s.csv'%(i))

