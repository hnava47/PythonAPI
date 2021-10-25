import xml.etree.ElementTree as et

# Oracle web service response
xml = '''------=_Part_24011_2091722813.1635094866364
Content-Type: application/xop+xml;charset=UTF-8;type="text/xml"
Content-Transfer-Encoding: 8bit
Content-ID: <bb200b30-fb49-4faf-badf-4ccc43f3f757>

<?xml version="1.0" encoding="UTF-8" ?>
<env:Envelope xmlns:env="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing"><env:Header><wsa:Action>http://xmlns.oracle.com/apps/financials/commonModules/shared/model/erpIntegrationService//ErpIntegrationService/importBulkDataResponse</wsa:Action><wsa:MessageID>urn:uuid:bea5f111-d327-4a2f-b4de-a026b0035db7</wsa:MessageID></env:Header><env:Body><ns0:importBulkDataResponse xmlns:ns0="http://xmlns.oracle.com/apps/financials/commonModules/shared/model/erpIntegrationService/types/"><result xmlns="http://xmlns.oracle.com/apps/financials/commonModules/shared/model/erpIntegrationService/types/">8673903</result></ns0:importBulkDataResponse></env:Body></env:Envelope>
------=_Part_24011_2091722813.1635094866364--
'''

# Parse XML string
root = et.fromstring(xml[192:len(xml)-47])

# Find ESS process number in XML tree
process = root.findall('.//')[5].text

print(process)
