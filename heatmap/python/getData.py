import requests
import json

# Coffeeshop v5 data
# X-Axis ending: 48,48
# Y-Axis ending: -30
# Reduced image has 400px less



def ConversionY(y):
    if (y > 0):
        beforeConversion = 26.8+y
    else:
        #negSum = -30 - y
        beforeConversion = -y
    #return (beforeConversion * 16.5) + 425
    return (beforeConversion * 16.5) + 25

def ConvertX(x):
    
    return x*15.2 + 40

appId = "ytcAgT6GaEXeDYNQRpTPWnz4daYTL37CCEnuig2n"
apiKey = "nU9X0fbcggiheoAZugoShpQzn2AAQrBsuLWJa7jp"
#maxRequests = count / 100
maxRequests = 10

url = "https://parseapi.back4app.com/classes/Playtest?where={\"levelId\":\"coffeeshop-v5\", \"playerId\":\"bryce\", \"action\":\"caught\"}"
#url = "https://parseapi.back4app.com/classes/Playtest?where={\"levelId\":\"coffeeshop-v5\", \"action\":\"caught\"}"

d = {}
_url = url
r = requests.get(url = _url,  headers={"X-Parse-Application-Id": appId, "X-Parse-REST-API-Key": apiKey}, params={"count":1})
data = json.loads(r.content)
numberOfResults = data["count"]
maxRequests = numberOfResults / 100
#print data

if (maxRequests == 0 and numberOfResults > 0):
    maxRequests = 1

for i in range(0, maxRequests):
    skip = i * 100
    _url = url+"&skip="+str(skip)
    r = requests.get(url = _url,  headers={"X-Parse-Application-Id": appId, "X-Parse-REST-API-Key": apiKey})
    data = json.loads(r.content)
    results = data["results"]
    for result in results:
        
        y = result["position"][2]
        x = result["position"][0]
        
        if (y < 0):
            newY = int(ConversionY(y))
            if (newY < 0):
                continue

            newX = int(ConvertX(x))
            key = str(newX)+","+str(newY)
            if key not in d.keys():
                d[key] = 1
            else:
                if (d[key] < 5):
                    d[key] += 1
            

for key, value in d.items():
    arrayKey = key.split(",")
    xValue = arrayKey[0]
    yValue = arrayKey[1]
    
    print "{ x:"+xValue+", y: "+yValue+", value: "+str(value)+"}"    
        



    #print r.content




#Need to sum Y 30+(oldY)
# y factor - 15,33

#beforeConversionY = 30+oldY
#newY = beforeConversionY*15,33


#MAX X = 510
#x factor = 10.2