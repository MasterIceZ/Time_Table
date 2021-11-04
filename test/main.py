import requests
import datetime
import os

res = requests.get('https://Table.aiceaeng.repl.co')
if str(res) != '<Response [200]>':
    url = "https://notify-api.line.me/api/notify"
    token = os.getenv('LINE_TOKEN')
    headers = {'content-type':'application/x-www-form-urlencoded', 'Authorization': 'Bearer ' + token}
    msg = 'Bot is Down! at ' + str(datetime.datetime.now())
    r = requests.post(url, headers=headers, data={'message':msg})
print(res)
print(datetime.datetime.now())
