class VulDocker:
    def __init__(self):
        self.network_mode = "bridge"
        self.ports = None
        pass

    def init_docker(self):
        pass


from .database import RedisUnAuth, MysqlFakePass, MemcachedUnAuth, MongoUnauth, PostgresqlUnauth
from .proxy import Socks5, HTTPProxy
from .service import SSHFakePass, FTPFakePass, RDPY
from .web import DVWA, SQLInjLib, FakeWebApp

vuls = [DVWA(), SSHFakePass(), FTPFakePass(), RedisUnAuth(), MysqlFakePass(), MemcachedUnAuth(), SQLInjLib(),
        FakeWebApp(), MongoUnauth(), PostgresqlUnauth(), RDPY(), Socks5(), HTTPProxy()]
