# coding:utf-8
import unittest
import requests
from ddt import ddt,file_data

@ddt
class MyTestCase(unittest.TestCase):

    @file_data("api_ddt.json")
    def test_01_something(self,phone):
        url = "http://apis.juhe.cn/mobile/get"
        payload = {
            "phone": phone,
            "key": "802831374e480e92f88f1bd989a805b0"
        }
        resq = requests.get(url, params=payload)
        resq.encoding = "utf-8"
        resq_jsondata = resq.json()
        if resq_jsondata['reason']=="Return Successd!":
            print(resq_jsondata["result"]["province"],resq_jsondata["result"]["city"])
        else:
            print(resq_jsondata["reason"])

    @file_data("api_ddt_key.json")
    def test_02something(self,key):
        url = "http://apis.juhe.cn/mobile/get"
        payload = {
            "phone": "1806250",
            "key": key
        }
        resq = requests.get(url, params=payload)
        resq.encoding = "utf-8"
        resq_jsondata = resq.json()
        if resq_jsondata['reason'] == "Return Successd!":
            print(resq_jsondata["result"]["province"], resq_jsondata["result"]["city"])
        else:
            print(resq_jsondata["reason"])



if __name__ == '__main__':
    unittest.main()
