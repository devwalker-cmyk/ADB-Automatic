

from abc import ABC, abstractmethod
import typing as t
import requests
import json
from ..exceptions import ProxyException
from ..model import IProxy



class BaseServiceProxy(ABC):
    """Abstract proxy service."""
    url : str
    def __init__(
            self, 
            data : dict,
            *, 
            retry: int = 3,
            status_on_callback: t.Optional[callable] = None):
        if status_on_callback is None:
            self.status_on_callback = self._status_on_callback
        

        self._proxy = None
        self._retry = retry
        self._data = data
        self._session = requests.Session()
        self._session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json"
        })

        

    @property
    def proxy(self):
        return self._proxy
    
    @proxy.setter
    def proxy(self, value):
        self._proxy = value


    def request(self, method : str, url : str, **kwargs):
        """Make a request to the proxy service."""
        retry = self._retry
        while retry > 0:
            try:
                response = self._session.request(method, url, **kwargs)
                if response.status_code == 200:
                    return response.json()
                
                self.status_on_callback(f"Failed to connect to {url} ({response.status_code}) ({response.text})")
                
            except Exception as e:
                retry -= 1
                self.status_on_callback(f"Failed to connect to {url} ({retry} retries left).")
        else:
            raise ProxyException("Failed to connect to proxy service.")
        

    def _status_on_callback(self, message: str):
        """Callback function for status on."""

    @abstractmethod
    def get_proxy(self) -> t.Optional[IProxy]:
        """Get a proxy object."""
        pass

    @abstractmethod
    def change_proxy(self) -> t.Optional[IProxy]:
        """Change the proxy object."""
        pass
