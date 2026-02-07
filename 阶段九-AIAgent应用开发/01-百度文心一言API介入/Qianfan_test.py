import requests
import json
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

client_id = os.getenv('BAIDU_QIANFAN_CLINE_AK')
client_secret = os.getenv('BAIDU_QIANFAN_CLINE_SK')

def get_access_token():
    url = f"https://aip.baidubce.com/oauth2/token?grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}"

    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.json().get('access_token'))

def main():
    url = "https://qianfan.baidubce.com/v2/chat/completions_pro?access_token=" + get_access_token()

    payload = json.dumps({
        "message": [
            {
                "role": "user",
                "content": "介绍一下自己"
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


if __name__ == '__main__':
    main()