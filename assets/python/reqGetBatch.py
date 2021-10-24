# python3 -m pip install requests

import requests as r
import base64 as b64
import variables as v
import json

def getJeBatch(url, username, password):
    env = url + '/fscmRestApi/resources/11.13.18.05/journalBatches'

    credentials = b64.b64encode(bytes(username+':'+password, encoding='UTF-8')).decode()
    authorization = f'Basic {credentials}'

    payload={}
    headers = {
    'Content-Type': 'application/vnd.oracle.adf.resourcecollection+json',
    'Authorization': authorization
    }

    response = r.request('GET', env, headers=headers, data=payload)

    return response.text

print(getJeBatch(v.Dev3Url, v.OraUsername, v.OraPassword))
