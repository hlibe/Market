#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 27 09:26:50 2021

@author: HaoLI
"""
from futu import *
trd_ctx = OpenHKTradeContext(host='127.0.0.1', port=11111, security_firm=SecurityFirm.FUTUSECURITIES)
ret, data = trd_ctx.history_deal_list_query()
if ret == RET_OK:
    print(data)
    if data.shape[0] > 0:  # 如果成交列表不为空
        print(data['deal_id'][0])  # 获取历史成交的第一个成交号
        print(data['deal_id'].values.tolist())  # 转为 list
else:
    print('history_deal_list_query error: ', data)
trd_ctx.close()