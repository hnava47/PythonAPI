#Using Python standard library

import http.client as hc
import base64 as b64
import variables as v
import json

def getJeBatch(url, username, password):

    credentials = b64.b64encode(bytes(username+':'+password, encoding='UTF-8')).decode()
    authorization = f'Basic {credentials}'

    conn = hc.HTTPSConnection(url)
    payload = ''
    headers = {
    'Content-Type': 'application/vnd.oracle.adf.resourcecollection+json',
    'Authorization': authorization
    }
    conn.request("GET", "/fscmRestApi/resources/11.13.18.05/accountingPeriodsLOV", payload, headers)
    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")

# URL variable contains https:// which needs to be removed for function
print(getJeBatch(v.Dev3Url[8:], v.OraUsername, v.OraPassword))
