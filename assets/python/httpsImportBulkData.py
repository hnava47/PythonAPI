import http.client as hc
import base64 as b64
import xml.etree.ElementTree as et
import variables as v

def importBulkData(url, username, password):

    # Base 64 encoding authentication as 'Basic username:password'
    credentials = b64.b64encode(bytes(username+':'+password, encoding='UTF-8')).decode()
    authorization = f'Basic {credentials}'

    # Establishing connection to Oracle environment
    conn = hc.HTTPSConnection(url)

    # Oracle web service XML payload
    payload = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:typ="http://xmlns.oracle.com/apps/financials/commonModules/shared/model/erpIntegrationService/types/" xmlns:erp="http://xmlns.oracle.com/apps/financials/commonModules/shared/model/erpIntegrationService/">
        <soapenv:Header/>
        <soapenv:Body>
            <typ:importBulkData>
                <typ:document>
                    <erp:Content>UEsDBBQACAAIAK1bG1MAAAAAAAAAAMA1AAAjACAAR2xJbnRlcmZhY2VfSVNSX1JFVkVSU0FPX0pBTl8yMS5jc3ZVVA0AB/YgKWEDISlhAyEpYXV4CwABBPUBAAAEFAAAAO2ZXWujQBSG7xf2P8zVfsCYzoefvTPGtJaSBE0pvSoSp91AqkHNwv77HdtA7WYDa20Sxz0SkhHHmcnMwznn5Z34txgzwugZqT7Yy9KfIi+WWYojscjSJM5/4eA62vZhZ5RhV94Q+UvkhRllnNKXNql977sMnesD5lTNUFRTiUIbD++DKLyPfO+bnOr7OXK9iRbOQ80gOprl2YMoqhXFK/QgBIoXi3wj2yOx+MoIita5iJPihxAlcpHDCDeR6dgOYY6Onxs6odpVtsmrAYKndZaXb16y5L/hFiXmeW1JTVbgbm/l2pGX5XKCuBSIU23ke5p8TmvrsOSAnNt6kwme9213BKpF4+hN9yiN1+UGXZfJ4I9dl4ekG6Zly32fhYHn37pzP7yc3sgtn05nfhjtOS15LHJ1y6eKAoyv4lRjFPuT0edPk2ODY1oOG9gmgNMaHKZ5wfz/AYdWTwcvHYCcVuRwzd0ky7I5O36eFiX6gu6yTfp4VGRMZlBsckYo+XdkalkKiGmXpAxls9SWHN6MnFq0AXTapSldxWhjkubR5rW0AWTaRRtT0dKGg5g6LTn6TpoaD1FQ5LFYoctslSzTx6KvEBlQHn8MRMZfElZjjE6VvN5JD8jyj6JnN3epGIJAb522ArJ6kcjep71eMxlQ1E56KZ7JQIadNgjZaqWyi+FshyJCQZL139+6GHYGHCikVfK3OgQO+Ftq+FuHQQb0Vv/9rYOSA/5WL/2tQzEDwqrv/laHShsQU6r6W12CCPwt1fytDtEDslxVfwv0Vg8hOrq/1SXtBf6Wcv4WyLAe4nN0f2s/Rb8BUEsHCDmSj3tmAgAAwDUAAFBLAwQUAAgACACtWxtTAAAAAAAAAABwAQAALgAgAF9fTUFDT1NYLy5fR2xJbnRlcmZhY2VfSVNSX1JFVkVSU0FPX0pBTl8yMS5jc3ZVVA0AB/YgKWEDISlhpSEpYXV4CwABBPUBAAAEFAAAAGNgFWNnYGJg8E1MVvAPVohQgAKQGAMnEBsxMDDaAWkgn7GAgSjgGBISBGGBddwB4iloSpih4gIMDFLJ+bl6iQUFOal6OYnFJaXFqSkpiSWpygHBULVvgNiDgYEfoS43MTkHYr4JkLBhYBBFyBWWJhYl5pVk5qUyMCtqJoJU5d2xE4FY6ucgo68U5H2pUUiJW3u6731mBn9ej8hv7Y4bV5lnpp7m7w4gxn+F+gYGFobWZoZGlgZpiUbWzhlF+bmp1o4G5o6mLgbGuiYWrma6JpZmJrpOluYGuqam5q5Gho4mFiaOBgwAUEsHCPM9QgzmAAAAcAEAAFBLAQIUAxQACAAIAK1bG1M5ko97ZgIAAMA1AAAjACAAAAAAAAAAAAC0gQAAAABHbEludGVyZmFjZV9JU1JfUkVWRVJTQU9fSkFOXzIxLmNzdlVUDQAH9iApYQMhKWEDISlhdXgLAAEE9QEAAAQUAAAAUEsBAhQDFAAIAAgArVsbU/M9QgzmAAAAcAEAAC4AIAAAAAAAAAAAALSB1wIAAF9fTUFDT1NYLy5fR2xJbnRlcmZhY2VfSVNSX1JFVkVSU0FPX0pBTl8yMS5jc3ZVVA0AB/YgKWEDISlhpSEpYXV4CwABBPUBAAAEFAAAAFBLBQYAAAAAAgACAO0AAAA5BAAAAAA=</erp:Content>
                    <erp:FileName>WebServiceTest2.zip</erp:FileName>
                    <erp:ContentType>zip</erp:ContentType>
                    <erp:DocumentTitle>GLInterface</erp:DocumentTitle>
                    <erp:DocumentAuthor>hectornava</erp:DocumentAuthor>
                    <erp:DocumentSecurityGroup>FAFusionImportExport</erp:DocumentSecurityGroup>
                    <erp:DocumentAccount>fin$/generalLedger$/import$</erp:DocumentAccount>
                </typ:document>
                <typ:jobDetails>
                    <erp:JobName>oracle/apps/ess/financials/generalLedger/programs/common,JournalImportLauncher</erp:JobName>
                    <erp:ParameterList>#NULL,Conversion,-1,123456789,N,N,N</erp:ParameterList>
                </typ:jobDetails>
                <typ:notificationCode>30</typ:notificationCode>
                <typ:callbackURL></typ:callbackURL>
                <typ:jobOptions></typ:jobOptions>
            </typ:importBulkData>
        </soapenv:Body>
        </soapenv:Envelope>'''

    # Web service required headers
    headers = {
    'Content-Type': 'text/xml;charset=UTF-8',
    'Authorization': authorization
    }

    # Invoke web service call
    conn.request("POST", "/fscmService/ErpIntegrationService?WSDL=null", payload, headers)
    res = conn.getresponse()
    data = res.read()

    xml = data.decode("utf-8")
    root = et.fromstring(xml[196:len(xml)-47])

    # Return ESS process ID
    return root.findall('.//')[5].text

# URL variable contains https:// which needs to be removed for function
print(importBulkData(v.Dev3Url[8:], v.OraUsername, v.OraPassword))
