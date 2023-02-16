import requests
import time
    
payload = {
        'content': "TEXT"
}

header = {
    'authorization': 'TOKEN'
}

r=requests.post("channelid",
                     json=payload, headers = header)
def sendMessege():
   while True:
       requests.post("channelid", json=payload, headers = header)
       time.sleep(delay)
    
sendMessege()
quit()