import time
import requests

from hashlib import sha1
import json
import hashlib
client = "yunhui"
host = "81.68.239.165:9083"

# 获取商品名称
def getProductName(productId):
    timestamp = time.time()
    ts = int(timestamp)

    # 需要加密的字符串
    pwd = "{0}_{1}".format(client, ts)
    # 创建sha1对象
    s1 = sha1()
    # 对s1进行更新
    s1.update(pwd.encode())
    # 加密处理
    sign = s1.hexdigest()

    url = "http://{0}/getProductName?productId={1}&client={2}&ts={3}&sign={4}".format(host, productId,client, ts, sign)
    print(url)
    resp = requests.get(url)
    print(resp.text)

# 获取商品销量信息
def sales(productId):
    timestamp = time.time()
    ts = int(timestamp)

    # 需要加密的字符串
    pwd = "{0}_{1}".format(client, ts)
    # 创建sha1对象
    s1 = sha1()
    # 对s1进行更新
    s1.update(pwd.encode())
    # 加密处理
    sign = s1.hexdigest()

    url = "http://{0}/sales?productId={1}&client={2}&ts={3}&sign={4}".format(host, productId,client, ts, sign)
    print(url)
    resp = requests.get(url)
    print(resp.text)

# 获取商品详情sku
def getDetail(productId):
    timestamp = time.time()
    ts = int(timestamp)

    # 需要加密的字符串
    pwd = "{0}_{1}".format(client, ts)
    # 创建sha1对象
    s1 = sha1()
    # 对s1进行更新
    s1.update(pwd.encode())
    # 加密处理
    sign = s1.hexdigest()

    url = "http://{0}/getDetail?productId={1}&client={2}&ts={3}&sign={4}".format(host, productId,client, ts, sign)
    print(url)
    resp = requests.get(url)
    print(resp.text)


def getMtopApi(api, data, v):
    timestamp = int(time.time()*1000)
    postData = {
        "data":  data,
        "api": api,
        "ttid":"10003226@tvtaobao_android_7.1.0",
        "v":v,
        "useWua":"1",
        "hasExtParams":"1"
    }

    group = "tbtv"
    action = "registerGetData"

    pwd = "{0}_{1}".format(client, timestamp)
    # 创建sha1对象
    s1 = sha1()
    # 对s1进行更新
    s1.update(pwd.encode())
    # 加密处理
    sign = s1.hexdigest()
    requestUrl = "http://81.68.239.162:9083/taobao?group={0}&action={1}&client={2}&time={3}&sign={4}".format(group,action, client, timestamp, sign)
    print(requestUrl)
    headers = {
        "user-agent": "taobao"
    }
    print(postData)
    result = requests.post(requestUrl, data=postData, headers=headers, timeout=20)
    print(result.text)

# 天猫搜索
def tmal_search():
    data = '''{

  "apptimestamp": "1619073204",
  "info": "wifi",
  "isBeta": "false",
  "jarvis_model_version": "mainse_rerank.alinn:20200711",
  "n": "10",
  "page": "1",
  "q": "美妆蛋",
  "rainbow": "8462102,14477,14957,14963,10287578,14355,14899,14071,12995,10073442",
  "search_action": "initiative",
  "sversion": "10.4",
  "tab": "newmall",
  "ttid": "270200@taobao_android_9.12.0",
  "utd_id": "XyJ/Q0W+uf8DAIcmHzh0Hb/o",
  "vm": "nw"
}'''
    v = "1.0"
    api = "mtop.taobao.wsearch.appsearch"
    jobj = json.loads(data)
    jobj["q"] = "美妆蛋"
    jobj["apptimestamp"] = int(time.time())
    getMtopApi(api, json.dumps(jobj), v)


if __name__ == '__main__':

    getDetail("612311328322")