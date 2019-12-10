from vulns import VulDocker
from vulns.util import ONE_DAY


class Socks5(VulDocker):
    def __init__(self):
        super().__init__()
        self.name = 'socks5'
        self.docker_image = 'serjs/go-socks5-proxy'
        self.recreate_time = ONE_DAY
        self.ports = {"1080": 1080}

    def __repr__(self):
        return "一个开放的socks5服务。"


class HTTPProxy(VulDocker):
    def __init__(self):
        super().__init__()
        self.name = 'http_proxy'
        self.docker_image = 'sameersbn/squid:3.5.27-2'
        self.recreate_time = ONE_DAY
        self.ports = {"3128": 3128}

    def __repr__(self):
        return "一个开放的HTTP代理服务"
