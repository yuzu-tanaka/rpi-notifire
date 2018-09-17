#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import with_statement

import urllib
import urllib2
import xml.etree.ElementTree as ET
import pymongo
import csv
import time
import datetime

tree = ET.parse('../00_common/settings/ServerSetting.xml')
root = tree.getroot()
MONGO_IP = root.findtext('.//all/mongo_ip')
MONGO_DB_NAME = root.findtext('.//mongo/name')

class CrewButton(object):
    def __init__(self, port=27017):
        self.__client = pymongo.MongoClient(host=MONGO_IP, port=port)
        self.__db = self.__client[MONGO_DB_NAME]
        self.__crew_entry_history = self.__db.crew_entry_history

    def insert(self):
        timestamp = datetime.datetime.utcnow()
        self.__crew_entry_history.insert_one({'timestamp':timestamp, 'trackerID':''})

if __name__ == "__main__":
    button = CrewButton()
    button.insert()
