# -*- coding: utf-8 -*-
# -*- coding: euc-kr-*-
import csv
import sqlite3
import os
from datetime import datetime, timedelta

directory = sqlite3.connect(os.getenv("APPDATA") + "\..\Local\Google\Chrome\User Data\Default\history")
directory.text_factory = str
cur = directory.cursor()
output = open('download.csv', 'wb')
csv_writer = csv.writer(output)
headers = ('Time','downloads_path', 'downloas_url', 'downloadsbyte')
csv_writer.writerow(headers)
dt = datetime(1970, 1, 1)

for row in (cur.execute('SELECT datetime(((downloads.start_time/1000000)-11644473600), "unixepoch"), downloads.target_path, downloads_url_chains.url, downloads.total_bytes \
FROM downloads, downloads_url_chains WHERE downloads.id = downloads_url_chains.id;')):
    row = list(row)
    print row
    csv_writer.writerow(row)

