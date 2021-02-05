import requests
TOKEN = "xapp-1-A01LV8QPBNH-1725022059985-52a799fb68b460bac083976c96cbb0c1512c7ac6dcf745aac4121683dcac9314"
CHANNEL_ID = 'C018ZT7TYMN'
URL = "https://slack.com/api/channels.history"
TOKEN = "xxxx_YOUR_TOKEN_xxxx"
from datetime import datetime

def main():


    oldest=datetime(2021,2,5).timestamp()
    latest = datetime(2021,2,6).timestamp()
    payload = {
        'token': TOKEN,
        'channel': CHANNEL_ID,
        'latest': str(latest),
        'oldest': str(oldest)
    }

    r = requests.get(URL, params=payload)
    print(r.json())

main()
