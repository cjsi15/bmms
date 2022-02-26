import json

file={}
with open('masterfile.json','w') as q:
        json.dump(data,q,indent=4)
        print("Success")

class Stocks:
    def __init__(self,id,name,quantity,remarks):
        self.id=id
        self.name=name
        self.quantity=quantity
        self.remarks=remarks

    @property
    def addstocks(self):
        return self.name,self.quantity,self.remarks

    @property
    def itemcode(self):
         return self.id

    def addinventory():
        data=Stocks('1','Meter','12','Good Condition')
        data.addstocks
        file[data.itemcode]=data.addstocks
        print(data.addstocks)
        print(file)
        


