import json
file={}

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
        with open('masterfile.json','r') as y:
            file=json.load(y)
        data=Stocks('1','Meter','12','Good Condition')
        data.addstocks
        file[data.itemcode]=data.addstocks
        with open('masterfile.json','w') as q:
            json.dump(file,q,indent=4)
        print(data.addstocks)
        print(file)


