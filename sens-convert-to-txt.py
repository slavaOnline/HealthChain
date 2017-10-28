import serial 
import time
import json

r = serial.Serial("com4", 9600)
temps = []
timeTemp1 = 0
timeTemp2 = 0
id_ = "#012312341243"
key_ = "123"
valuesObject = []
valuesList = []

def temp(arr):
    mean = sum(arr)/len(arr)
    return mean

def jsonConverter(id_, key, values):
    return json.dumps({"id": id_, "key": key_, "values": values})
    

while True:
        
        time.sleep(1)
        timeTemp1 = timeTemp1 + 1
        timeTemp2 = timeTemp2 + 1
        t = float(r.readline())
        temps.append(t)
        
        if timeTemp1 >= 4 :
            valuesObject.append("%.1f" % (temp(temps)))
            valuesObject.append(time.time())
            valuesList.append(valuesObject)
            print(valuesObject)
           
            timeTemp1 = 0
            
        
        
        
        if timeTemp2 >=12:
            print()
            print(jsonConverter(id_,key_, valuesList))
            print()
            timeTemp2 = 0
            del valuesList[:]
        
        del valuesObject[:]
        del temps[:]    
            
       