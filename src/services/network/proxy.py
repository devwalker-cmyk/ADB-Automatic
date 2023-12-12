
from abc import ABC, abstractmethod
import typing as t

from src.services.network.model import IProxy



class ServiceProxy(ABC):
    """Abstract proxy service."""
    url : str

    def __init__(self, status_on_callback: t.Optional[callable] = None):
        if status_on_callback is None:
            self.status_on_callback = self._status_on_callback
        

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






class ServiceManager(ABC):
    """Abstract proxy service manager."""

    @abstractmethod
    def get_proxy(self) -> t.Optional[IProxy]:
        """Get a proxy object."""
        pass

    @abstractmethod
    def change_proxy(self) -> t.Optional[IProxy]:
        """Change the proxy object."""
        pass

    @abstractmethod
    def get_status(self) -> str:
        """Get the status of the proxy service."""
        pass