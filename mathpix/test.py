import base64
import json
import time

import requests

start = time.time()
file_path = 'images/anh6.jpg'
with open(file_path, "rb") as f:
    encode = str(base64.b64encode(f.read()))
image_uri = 'data:image/jpg;base64,' + encode[2:-1]
data_json = '{"src": "' + image_uri + '", "formats": ["latex_styled"]}'
r = requests.post("https://api.mathpix.com/v3/latex",
                  data=data_json,
                  headers={"app_id": "dinhvankiet124_gmail_com", "app_key": "7c7786b646d3bd31a0f2",
                           "Content-type": "application/json"})

print(time.time() - start)
res = json.loads(r.text)
print(res)
print(res['latex_styled'])
