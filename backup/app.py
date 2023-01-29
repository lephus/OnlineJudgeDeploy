# save this as app.py
from flask import Flask
import atexit
from datetime import datetime
import subprocess
import requests
# Schedule Library imported
from apscheduler.schedulers.background import BackgroundScheduler
import os

tryhardcodeToken = 'bot5802409922:AAGxiIP3XzJ0j1hQc5Zsokmb8o_ktSfp4c4'
chatId = '-688415700'

def removeFile(fileUrl):
    try:
        if os.path.exists(fileUrl):
            os.remove(fileUrl)
        else:
            print("The file at: "+fileUrl+" does not exist")
    except:
        print('PermissionError: [WinError 32] The process cannot access the file because it is being used by another process')

def backupData():
    now = datetime.now()
    d = now.strftime("%m-%d-%Y")
    filename = "tryhardcode_bk"+str(d)+"-"+str(now.timestamp())+".sql"
    dockerShell = "docker exec -it oj-postgres pg_dumpall -c -U onlinejudge > "+str(filename)
    subprocess.run(
        ["powershell", dockerShell], shell=True)
    file={'document':open(str(filename))}
    #https://api.telegram.org/bot{HTTP_API_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={MESSAGE_TEXT}
    resp = requests.post('https://api.telegram.org/'+tryhardcodeToken+'/sendDocument?chat_id='+chatId, files=file)
    removeFile(filename)
    return resp.content

scheduler = BackgroundScheduler()
scheduler.add_job(func=backupData, trigger="interval", seconds=24*60*60)
scheduler.start()
# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())

app = Flask(__name__)


@app.route("/backup-now")
def backupDataNow():
    return backupData()

@app.route('/')
def hello():
    return 'Hello'

app.run(host='0.0.0.0', port=81)
