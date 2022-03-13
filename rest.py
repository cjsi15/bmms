import json
from urllib.request import urlopen
#from methods import Stocks
#unique_id=[]
#itemcode=123
#name='handrill'
#qty=12
#remarks='Good'
#run=Stocks.addinventory(124,'Drill Bit',10,'Good')
file={}
url = 'http://localhost:8080/view'
response = urlopen(url)
string = response.read().decode('utf-8')
json_obj = json.loads(string)
for x  in json_obj:
    for a,b in x.items():
        file[a]=b
with open("data.json","w") as f:
    json.dump(file,f)
