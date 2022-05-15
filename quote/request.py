from urllib import request
import json



api_key = ['QUOTE_API_KEY']
class Request:

    def __init__(self): 
        pass

    def request(self,url,category):
        self.base_url=url
        self.req=request.urlopen(self.base_url.format(category,api_key))
        resp=self.req.read()
        data=json.loads(resp)
        return data
object=Request()