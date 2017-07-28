# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-
import csv
import sqlite3
import os
from datetime import datetime, timedelta

directory = sqlite3.connect(os.getenv("APPDATA") + "\..\Local\Google\Chrome\User Data\Default\history")
directory.text_factory = str
cur = directory.cursor()
output = open('weburllist.csv', 'wb')
csv_writer = csv.writer(output)
headers = ('URL', 'Title', 'Visit Count', 'Date')
csv_writer.writerow(headers)
dt = datetime(1601, 1, 1)

for row in (cur.execute('select url, title, visit_count, last_visit_time from urls')):
    row = list(row)
    url_time = dt + timedelta(microseconds=row[3])
    row[3] = url_time
    csv_writer.writerow(row)

