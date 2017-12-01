#!/usr/bin/env python

# encoding: utf-8

'''

@author: SunGuoTao

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: GuotaoSunVipSystem@gmail.com

@software: garner

@file: Test.py

@time: 2017/12/1 11:07

@desc:

'''
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
    app.run(debug=True)