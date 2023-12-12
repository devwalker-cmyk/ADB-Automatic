


import typing as t

from ..base import BaseServiceProxy

class TinsoftProxy(BaseServiceProxy):
    url = "https://proxy.tinsoftsv.com/api"
    
    def __init__(self, api_key: str, status_on_callback: t.Optional[callable] = None):
        super().__init__({
            "api_key": api_key
        }, status_on_callback)

    
    def get_proxy(self):
        url = self.url + "changeProxy.php?key={api_key}".format(**self._data)
        response = self.request("GET", url)
        if response["success"]:
            pass

