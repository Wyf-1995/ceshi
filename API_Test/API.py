import requests
import  json

url = "http://apis.juhe.cn/mobile/get"

querystring = {"phone":"18845091","key":"802831374e480e92f88f1bd989a805b0"}

headers = {
    'User-Agent': "PostmanRuntime/7.15.2",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "2bba4b9d-6fca-40c5-9e8d-b6df09085919,307df0b6-e370-411f-b1e0-0840402272d9",
    'Host': "apis.juhe.cn",
    'Cookie': "aliyungf_tc=AQAAAIr0BTOwWg4AMwavb/ElFQDiyvx6",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

json_dic=json.loads(response.text)
print(json_dic)
print(type(json_dic))
for i in json_dic:
    print(i,json_dic[i])