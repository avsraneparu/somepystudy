import io
import codecs
import json
#f = codecs.open('data.json', encoding='utf-8')
f = io.open('data.json', 'br')
for line in f:
    print(str(line, 'utf-8'))