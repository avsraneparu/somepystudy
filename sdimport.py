import json
from urllib.parse import quote

from six.moves.urllib.request import urlopen


DEFAULT_ENCODING='utf-8'
url = 'http://srv-ae:8080/api/v3/requests?OPERATION_NAME=GET_REQUEST&TECHNICIAN_KEY=F349DD34-7C2B-49E7-B016-2B919D3D7C28&ID=4'
urlResponse = urlopen(url)

#r = requests.get('http://srv-ae:8080/api/v3/requests?OPERATION_NAME=GET_REQUEST&TECHNICIAN_KEY=F349DD34-7C2B-49E7-B016-2B919D3D7C28&ID=4')
if hasattr(urlResponse.headers,'get_content_charset'):
    encoding = urlResponse.headers.get_content_charset('DEFAULT_ENCODING')
else:
    encoding = urlResponse.headers.getparam('charset') or DEFAULT_ENCODING
data = json.loads(urlResponse.read().decode(encoding))
#data_1251 = json.loads(urlResponse.read().decode()
#data=json.loads(json.dumps(r.json(),sort_keys=False,indent=4))

with open('data.json', 'w') as outfile:
    json.dump(data, outfile.encode('cp1251'), sort_keys=False, indent=4)
#json_data=json.loads(data)
#data.decode('utf-8').encode('cp1251', 'ignore')
print(data)

#print(data_1251)