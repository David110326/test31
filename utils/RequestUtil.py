import requests

def requests_get(url,headers):
    #发送请求
    r = requests.get(url,headers=headers)
    #获取结果内容
    code = r.status_code
    try:
        body = r.json()
    except Exception as e:
        body = r.text
    #内容存到字典
    res = dict()
    res['code'] = code
    res["body"] = body
    #返回字典
    return res

def requests_post(url,json=None,headers=None):
    # 发送请求
    r = requests.post(url,json=json,headers=headers)
    # 获取结果内容
    code = r.status_code
    try:
        body = r.json()
    except Exception as e:
        body = r.text
    # 内容存到字典
    res = dict()
    res['code'] = code
    res["body"] = body
    # 返回字典
    return res

#重构
class Request:
    def request_api(self,url,json=None,headers=None,method="get"):
        if method=="get":
            r = requests_get(url,headers)
        elif method=="post":
            r = requests_post(url)
        return r
    #重构get方法
    def get(self,url,**kwarg):
        return self.request_api(url,method="get",**kwarg)

    # 重构post方法
    def post(self, url, **kwarg):
        return self.request_api(url, method="post", **kwarg)


