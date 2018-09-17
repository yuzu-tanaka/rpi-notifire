#!/usr/bin/env python
# -*- coding: utf-8 -*-

# server.py
from flask import Flask, render_template, request

app = Flask(__name__)

# mongo-dbへの通知処理を行うところ
def notify(entryLeave):
    if entryLeave == 'entry':
        #進入時の通知処理
        ret = 'Entry'
    elif entryLeave == 'leave':
        #退出時の通知処理
        ret = 'leave'
    else:
        ret = None

    return ret


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/entry')
def entry():
    # request.argsにクエリパラメータが含まれている
    #val = request.args.get("msg", "Not defined")
    # ここに通知する処理を記述する
    ret = notify('entry')
    return ret

@app.route('/leave')
def hello():
    # request.argsにクエリパラメータが含まれている
    #val = request.args.get("msg", "Not defined")
    ret = notify('leave')
    return ret

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
