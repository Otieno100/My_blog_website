from urllib import request
import json

class Request:

    def __init__(self): 
        pass

    def request(self,url,category):
        self.base_url=url
        self.req=request.urlopen(self.base_url.format(category))
        resp=self.req.read()
        data=json.loads(resp)
        return data
obj=Request()