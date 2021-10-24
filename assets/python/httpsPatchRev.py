import http.client as hc
import base64 as b64
import variables as v
import json as j

def patchReversal(url, id, username, password):

    credentials = b64.b64encode(bytes(username+':'+password, encoding='UTF-8')).decode()
    authorization = f'Basic {credentials}'

    conn = hc.HTTPSConnection(url)

    payload = j.dumps({
    'ReversalFlag': 'Y',
    'ReversalPeriod': 'Feb-21',
    'ReversalMethodMeaning': 'Switch debit or credit'
    })

    headers = {
    'Content-Type': 'application/json',
    'Authorization': authorization
    }

    uri = f'/fscmRestApi/resources/11.13.18.05/journalBatches/{id}'

    conn.request("PATCH", uri, payload, headers)
    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")

# URL variable contains https:// which needs to be removed for function
print(patchReversal(v.Dev3Url[8:], 17015, v.OraUsername, v.OraPassword))
