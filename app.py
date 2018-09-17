#!/usr/bin/env python
# -*- coding: utf-8 -*-

# server.py
from flask import Flask, render_template, request
import datetime

# mongo db 
from pymongo import MongoClient
client = MongoClient('localhost', 27017) #接続先サーバ
db = client['testDatabase'] #データベース
collection = db['testCollection'] #コレクション


app = Flask(__name__)

def mongoPost(action): # 引数でアクションを渡して、それでmongoに書き込む
## ここに店員進入の通知を書き込む
    post = {"action": action,
    "tags": ["とりあえず", "なんか進入", "データ登録"],
    "date": datetime.datetime.utcnow()}
    try:
      result = collection.insert_one(post)
      print(post)
    except:
      print(result)
    return result

# mongo-dbへの通知処理を行うところ
def notify(entryLeave):

    if entryLeave == 'entry':
        #進入時の通知処理
        ret = mongoPost(entryLeave)
        ret = 'leave'
    elif entryLeave == 'leave':
        #退出時の通知処理
        ret = mongoPost(entryLeave)
        ret = 'entry'
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
    return render_template('entry.html', message=u'退出',action=ret)

@app.route('/leave')
def hello():
    # request.argsにクエリパラメータが含まれている
    #val = request.args.get("msg", "Not defined")
    ret = notify('leave')
    return render_template('entry.html', message=u'入店',action=ret)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8080)
