import requests, base64, variables as v

url = v.TestUrl + '/fscmService/AccountCombinationService?WSDL'

payload = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:typ="http://xmlns.oracle.com/apps/financials/generalLedger/accounts/codeCombinations/accountCombinationService/types/" xmlns:acc="http://xmlns.oracle.com/apps/financials/generalLedger/accounts/codeCombinations/accountCombinationService/">
    <soapenv:Header/>
    <soapenv:Body>
        <typ:validateAndCreateAccounts>
        <!--Zero or more repetitions:-->
            <typ:validationInputRowList>
            <!--Optional:-->
                <acc:DynamicInsertion>y</acc:DynamicInsertion>
                <!--Optional:-->
                <acc:Segment1>10067</acc:Segment1>
                <!--Optional:-->
                <acc:Segment2>0000</acc:Segment2>
                <!--Optional:-->
                <acc:Segment3>112532</acc:Segment3>
                <!--Optional:-->
                <acc:Segment4>0000</acc:Segment4>
                <!--Optional:-->
                <acc:Segment5>00000</acc:Segment5>
                <!--Optional:-->
                <acc:Segment6>00000</acc:Segment6>
                <!--Optional:-->
                <acc:Segment7></acc:Segment7>
                <!--Optional:-->
                <acc:Segment8></acc:Segment8>
                <!--Optional:-->
                <acc:Segment9></acc:Segment9>
                <!--Optional:-->
                <acc:Segment10></acc:Segment10>
                <!--Optional:-->
                <acc:Segment11></acc:Segment11>
                <!--Optional:-->
                <acc:Segment12></acc:Segment12>
                <!--Optional:-->
                <acc:Segment13></acc:Segment13>
                <!--Optional:-->
                <acc:Segment14></acc:Segment14>
                <!--Optional:-->
                <acc:Segment15></acc:Segment15>
                <!--Optional:-->
                <acc:Segment16></acc:Segment16>
                <!--Optional:-->
                <acc:Segment17></acc:Segment17>
                <!--Optional:-->
                <acc:Segment18></acc:Segment18>
                <!--Optional:-->
                <acc:Segment19></acc:Segment19>
                <!--Optional:-->
                <acc:Segment20></acc:Segment20>
                <!--Optional:-->
                <acc:Segment21></acc:Segment21>
                <!--Optional:-->
                <acc:Segment22></acc:Segment22>
                <!--Optional:-->
                <acc:Segment23></acc:Segment23>
                <!--Optional:-->
                <acc:Segment24></acc:Segment24>
                <!--Optional:-->
                <acc:Segment25></acc:Segment25>
                <!--Optional:-->
                <acc:Segment26></acc:Segment26>
                <!--Optional:-->
                <acc:Segment27></acc:Segment27>
                <!--Optional:-->
                <acc:Segment28></acc:Segment28>
                <!--Optional:-->
                <acc:Segment29></acc:Segment29>
                <!--Optional:-->
                <acc:Segment30></acc:Segment30>
                <acc:LedgerName>USA Primary</acc:LedgerName>
                <!--Optional:-->
                <acc:EnabledFlag>true</acc:EnabledFlag>
                <!--Optional:-->
                <acc:FromDate></acc:FromDate>
                <!--Optional:-->
                <acc:ToDate></acc:ToDate>
            </typ:validationInputRowList>
        </typ:validateAndCreateAccounts>
    </soapenv:Body>
</soapenv:Envelope>'''

credentials = base64.b64encode(bytes(v.OraUsername+":"+v.OraPassword, encoding="UTF-8")).decode()
authorization = 'Basic %s' % credentials

headers = {
    'Content-Type': 'text/xml;charset=UTF-8',
    'Authorization': authorization
}

response = requests.request('POST', url, headers=headers, data=payload)

print(response.text)
