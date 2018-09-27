import requests
import json

DEFAULT_ENCODING='utf-8'
r = requests.get('http://srv-ae:8080/api/v3/requests?OPERATION_NAME=GET_REQUEST&TECHNICIAN_KEY=F349DD34-7C2B-49E7-B016-2B919D3D7C28&ID=4')
if hasattr(r.headers,'get_content_charset'):
    encoding = r.headers.get_content_charset('DEFAULT_ENCODING')
else:
    encoding = DEFAULT_ENCODING
data=json.loads(json.dumps(r.json(),sort_keys=False,indent=4, ensure_ascii=False))
with open('data.json', 'w') as outfile:
    json.dump(data, outfile, sort_keys=False, indent=4, ensure_ascii=False)
print(data)

