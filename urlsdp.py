# -*- coding: utf-8 -*-
import codecs
import json
import urllib
from six.moves.urllib.request import urlopen

url = 'http://srv-ae:8080/api/v3/requests?OPERATION_NAME=GET_REQUEST&TECHNICIAN_KEY=F349DD34-7C2B-49E7-B016-2B919D3D7C28&ID=4'
uh = urllib.request.urlopen(url)
data = uh.read()
print ('Retrieved',len(data),'characters')
#print (codecs.decode(data).strip())

#js = json.loads(data.decode("utf-8"))
js = json.loads(codecs.decode(data))
print(list(js))