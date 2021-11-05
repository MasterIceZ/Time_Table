import requests
import datetime
import os
import pytz
import linenotif

res = requests.get('https://Table.aiceaeng.repl.co')
if str(res) != '<Response [200]>':
    noti = linenotif.Notify()
    noti.setKey(os.getenv('LINE_TOKEN'))
    noti.send_message('Bot Down!')
print(res)
print(datetime.datetime.now())
