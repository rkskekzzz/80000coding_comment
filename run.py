import os
import requests
import json

COMMENT_URL = os.environ['COMMENT_URL']
HOST_URL = os.environ['HOST_URL']
BEARER = os.environ['BEARER']

response = requests.get(COMMENT_URL)
responseJson = json.loads(response.text)

BODY = responseJson[-1]['body']
SENDER =  responseJson[-1]['user']['login']
DATABASE_ID = HOST_URL.split("/")[-1].replace("-","")

headers = {
    "Authorization": f"Bearer {BEARER}",
    "Accept": "application/json",
    "Notion-Version": "2022-0ㅇ2-22",
    "Content-Type": "application/json"
}

def updateComment():
    print(BODY)
    print(SENDER)
    print(DATABASE_ID)
    _apiUrl = "https://api.notion.com/v1/comments"
    _payload = {
        "parent": {
            "page_id": DATABASE_ID
        },
        "rich_text": [
            {
                "text": {
                    "content": BODY
                }
            },
            {
                "text": {
                    "content": "  by ",
                },
                "annotations": {
                    "bold": True,
                    "italic" : True
                }
            },
            {
                "text": {
                    "content": SENDER,
                    "link": {
                        "url" : "https://github.com/" + SENDER
                    }
                },
                "annotations": {
                    "bold": True,
                    "italic" : True
                }
            },
            {
                "text": {
                    "content": " ",
                },
            },
            {
                "text": {
                    "content": "from oopy",
                    "link": {
                        "url" : HOST_URL
                    }
                },
                "annotations": {
                    "bold": True,
                    "code" : True
                }
            }
        ]
    }
    response = requests.post(_apiUrl, data=json.dumps(_payload), headers=headers)
    responseJson = json.loads(response.text)
    print(responseJson)

updateComment()
