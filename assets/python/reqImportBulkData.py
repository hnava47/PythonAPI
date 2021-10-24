import requests, base64, csv, os
from urllib3.exceptions import InsecureRequestWarning

def payload(source, ledgerId, groupId, suspense, summary, flexfield):
    secondPayload = """             <typ:jobDetails>
                <erp:JobName>oracle/apps/ess/financials/generalLedger/programs/common,JournalImportLauncher</erp:JobName>
                <erp:ParameterList>#NULL,"""+str(source)+""","""+str(ledgerId)+""","""+str(groupId)+""","""+str(suspense)+""","""+str(summary)+""","""+str(flexfield)+"""</erp:ParameterList>
             </typ:jobDetails>\n"""
    return secondPayload

def invokeAPI(oraUser, oraPassword, oraUrl, directory, file, source, ledgerId, groupId, suspense, summary, flexfield):
    username = str(oraUser)
    password = str(oraPassword)

    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

    url = str(oraUrl)

    credentials = base64.b64encode(bytes(username+":"+password, encoding="UTF-8")).decode()
    authorization = "Basic {}".format(credentials)

    headers = {"Content-Type": "text/xml;charset=UTF-8", "Authorization": authorization}
    with open(directory, "rb") as f:
        readfile = f.read()
        encodedFile = base64.b64encode(readfile).decode()
        f.close()

    primaryPayload = """<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:typ="http://xmlns.oracle.com/apps/financials/commonModules/shared/model/erpIntegrationService/types/" xmlns:erp="http://xmlns.oracle.com/apps/financials/commonModules/shared/model/erpIntegrationService/">
       <soapenv:Header/>
       <soapenv:Body>
          <typ:importBulkData>
             <typ:document>
                <erp:Content>"""+str(encodedFile)+"""</erp:Content>
                <erp:FileName>"""+str(file)+"""</erp:FileName>
                <erp:ContentType>zip</erp:ContentType>
                <erp:DocumentTitle>GLInterface</erp:DocumentTitle>
                <erp:DocumentAuthor>"""+str(oraUser)+"""</erp:DocumentAuthor>
                <erp:DocumentSecurityGroup>FAFusionImportExport</erp:DocumentSecurityGroup>
                <erp:DocumentAccount>fin$/generalLedger$/import$</erp:DocumentAccount>
             </typ:document>\n"""

    with open("C:/ProgramData/Alteryx/Engine/importBulkData_glParam.csv") as paramFile:
        reader = csv.reader(paramFile)
        pList = list(reader)
        for f in range(1, len(pList)):
            if pList[f][3] == directory:
                primaryPayload += payload(str(pList[f][5]), str(pList[f][6]), str(pList[f][7]), str(pList[f][8]), str(pList[f][9]), str(pList[f][10]))
            else:
                continue
        paramFile.close()

    primaryPayload += """             <typ:notificationCode>30</typ:notificationCode>
             <typ:callbackURL></typ:callbackURL>
             <typ:jobOptions></typ:jobOptions>
          </typ:importBulkData>
       </soapenv:Body>
    </soapenv:Envelope>"""

    response = requests.post(url, data=primaryPayload, headers=headers, verify=False)

    if response.status_code == 200:
        return str(file)+": ESS Job Successfully Triggered!\n"
    elif response.status_code == 400:
        return str(file)+": ERROR Code: {} User Is Not Recognized\n".format(response.status_code)
    elif response.status_code == 401:
        return str(file)+": ERROR Code: {} User Is Not Recognized\n".format(response.status_code)
    elif response.status_code == 403:
        return str(file)+": ERROR Code: {} User Does Not Have Access\n".format(response.status_code)
    elif response.status_code == 404:
        return str(file)+": ERROR Code: {} URL Not Recognized\n".format(response.status_code)
    elif response.status_code == 407:
        return str(file)+": ERROR Code: {} Proxy Authentication Required\n".format(response.status_code)
    else:
        return str(file)+": ERROR Code: {} Internal Server Error\n".format(response.status_code)

with open("C:/ProgramData/Alteryx/Engine/importBulkData_glParam.csv") as csvFile:
    reader = csv.reader(csvFile)
    paramList = list(reader)
    with open("C:/Users/hnava002/Desktop/gl_importbulkdata.log", "w") as writeFile:
        r = 1
        while r < len(paramList):
            if r == 1:
                writeFile.write(invokeAPI(paramList[r][0], paramList[r][1], paramList[r][2], paramList[r][3], paramList[r][4], paramList[r][5], paramList[r][6], paramList[r][7], paramList[r][8], paramList[r][9], paramList[r][10]))
                r += 1
            elif paramList[r][3] != paramList[r-1][3]:
                writeFile.write(invokeAPI(paramList[r][0], paramList[r][1], paramList[r][2], paramList[r][3], paramList[r][4], paramList[r][5], paramList[r][6], paramList[r][7], paramList[r][8], paramList[r][9], paramList[r][10]))
                r += 1
            else:
                r += 1
                continue
        writeFile.close()
    csvFile.close()

os.remove("C:/ProgramData/Alteryx/Engine/importBulkData_glParam.csv")
os.remove("C:/ProgramData/Alteryx/Engine/glinvoke_importbulkdata.py")
