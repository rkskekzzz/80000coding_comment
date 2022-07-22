import os
import requests
import json

COMMENT_URL = os.getenv('COMMENT_URL')
HOST_URL = os.getenv('HOST_URL')
my_bearer = os.getenv("BEARER")

response = requests.request("GET", COMMENT_URL,)
responseJson = json.loads(response.text)

BODY = responseJson[-1]['body']
SENDER =  responseJson[-1]['user']['login']
DATABASE_ID = HOST_URL.split("/")[-1].replace("-","")




apiUrl = "https://api.notion.com/v1/comments"
headers = {
    "Authorization": "Bearer {}".format(my_bearer),
    "Accept": "application/json",
    "Notion-Version": "2022-02-22",
    "Content-Type": "application/json"
}

def updateComment():
    body = {
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
                        "url" : "https://80000coding.oopy.io/ddcdbb4d-461a-4a64-97b8-5040fc49c7d6"
                    }
                },
                "annotations": {
                    "bold": True,
                    "code" : True
                }
            }
        ]
    }
    response = requests.request("POST", apiUrl, headers=headers, data=json.dumps(body))
    responseJson = json.loads(response.text)

updateComment()