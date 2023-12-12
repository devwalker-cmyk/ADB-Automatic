




from dataclasses import dataclass
import typing as t



class IProxy(t.TypedDict):
    """Interface for proxy objects."""
    host: t.Required[str] 
    port: t.Required[int]
    username: t.Optional[str]
    password: t.Optional[str]
    timeout: t.Optional[int] 
    type: t.Literal["HTTP", "HTTPS", "SOCKS4", "SOCKS5"]
    


    



    

