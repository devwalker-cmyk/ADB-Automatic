







class ProxyException(Exception):
    """Base exception for all proxy exceptions"""
    pass


class ProxyTimeout(ProxyException):
    """Proxy timeout exception"""
    pass


class ProxyConnectionError(ProxyException):
    """Proxy connection error exception"""
    pass


class ProxyConnectionRefused(ProxyException):
    """Proxy connection refused exception"""
    pass