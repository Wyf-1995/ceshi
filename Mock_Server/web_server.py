# coding:utf-8
from flask import Flask ,request

app = Flask(__name__)

resp_dic_1 = {"code": 200,
            "data": {"customerNum": 1000, "contactsNum": 9527, "businessNum": 110, "contractNum": 120, "recordNum": 119,
                     "receivablesNum": 114, "businessStatusNum": 112}, "error": ""}

resp_dic_2 = {"code": 200,
            "data": {"customerNum": 500, "contactsNum": 9527, "businessNum": 110, "contractNum": 120, "recordNum": 119,
                     "receivablesNum": 114, "businessStatusNum": 112}, "error": ""}


@app.route("/", methods=["GET","POST"])
def hello():
    req = str(request.data).split('"')[3]
    print(req)
    if req =="today":
        return resp_dic_1
    elif req=="yesterday":
        return resp_dic_2
    else:
        return "你猜今天星期几"
    return resp_dic_1


if __name__ == '__main__':
    app.run()
