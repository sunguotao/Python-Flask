#!/usr/bin/env python

# encoding: utf-8

'''

@author: SunGuotao

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: GuotaoSunVipSystem@gmail.com

@software: garner

@file: Api.py

@time: 2017/11/30 上午11:44

@desc:

'''
from flask import Flask,jsonify,request
import pymongo
from scrapy.conf import settings
import json

BASE_DATA = {
    "code":200,
    "msg":"success",
}
PAGE_SIZE = 10

app = Flask(__name__)

def getFocusData(pageNum,pageSize):
    connection = pymongo.MongoClient(settings['MONGODB_HOST'], settings['MONGODB_PORT'])
    db = connection[settings['MONGODB_NAME']]
    focus_data = db[settings['MONGODB_DOCNAME']]
    dataList = []
    try:
        if int(pageNum) < 0:
            pageNum = 0
        else:
            pageNum = int(pageNum)

        if int(pageSize) < 0:
            pageSize = PAGE_SIZE
        else:
            pageSize = int(pageSize)

    except Exception as e:
        print('fuck')
        pageNum = 0
        pageSize = PAGE_SIZE

    if not focus_data.find():
        BASE_DATA['data'] = dataList
        BASE_DATA['msg'] = '数据库暂无数据'
        BASE_DATA['data'] = dataList
    else:
        temp = focus_data.find()[pageNum*pageSize : pageNum*pageSize+pageSize]
        print('temp',temp)
        if temp:
            for data in temp:
                data.pop('_id')
                dataList.append(data)
            BASE_DATA['data'] = dataList
        if len(BASE_DATA['data']) == 0:
            BASE_DATA['msg'] = '暂无更多数据'

    return BASE_DATA


@app.route('/focuslist',methods=['GET'])
def index():
    pageNum = request.args.get('pageNum')
    pageSize = request.args.get('pageSize',PAGE_SIZE)
    print('data',jsonify(getFocusData(pageNum,pageSize)))
    return jsonify(getFocusData(pageNum,pageSize))


if __name__ == '__main__':
    app.run(host='192.168.1.106',port=9090,debug=True)