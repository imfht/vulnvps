import time
from contextlib import suppress

import requests
from loguru import logger


class VulDocker:
    def __init__(self):
        self.network_mode = "bridge"
        self.ports = None
        pass

    def init_docker(self):
        pass


ONE_MIN = 60
ONE_HOUR = 60 * 60
ONE_DAY = 24 * ONE_HOUR


class DVWA(VulDocker):
    def __init__(self, **kwargs):
        super().__init__()
        self.name = 'dvwa'
        self.docker_image = 'imfht/dvwa-nologin:latest'
        self.ports = {'80/tcp': 9200}
        self.recreate_time = 1000 * ONE_DAY  # will 'never' recreate dvwa for some reason.

    def __repr__(self):
        return "dvwa: visit :9200"

    def init_docker(self):
        while True:
            with suppress(Exception):
                response = requests.post('http://127.0.0.1:9200/setup.php', data={'create_db': 1})
                if response.text != 'okay':
                    logger.info("setup.php do not return okay.")
                    raise ValueError("")
                logger.info("init dvwa db.")
                break
            logger.debug("waiting dvwa up")
            time.sleep(1)


class SSHFakePass(VulDocker):
    def __init__(self, **kwargs):
        super().__init__()
        self.name = 'ssh-fake-pass'
        self.docker_image = 'arvindr226/alpine-ssh:latest'
        self.ports = {'22/tcp': 2222}
        self.recreate_time = 2 * ONE_MIN  # rebuild every two minute.

    def __repr__(self):
        return "ssh: login as root/root"


class FTPFakePass(VulDocker):
    def __init__(self, **kwargs):
        super().__init__()
        self.name = 'ftp-fake-pass'
        self.docker_image = 'fauria/vsftpd:latest'
        self.ports = {'21/tcp': 21, '20/tcp': 20}
        self.recreate_time = 60 * 60  # rebuild every hour.
        self.environment = {'FTP_USER': 'test', 'FTP_PASS': '123456'}

    def __repr__(self):
        return 'ftp: login as test:123456'


class RedisUnAuth(VulDocker):
    def __init__(self):
        super().__init__()
        self.name = 'redis-unauth'
        self.docker_image = 'redis:latest'
        self.ports = {'6379/tcp': 6379}
        self.recreate_time = 10 * ONE_MIN  # 10 min

    def __repr__(self):
        return "redis: connect at :6379"


class MysqlFakePass(VulDocker):
    def __init__(self):
        super().__init__()
        self.name = 'mysql_fake_pass'
        self.docker_image = 'mysql:5'
        self.environment = {'MYSQL_ROOT_PASSWORD': 'root'}
        self.ports = {'3306': 3306}
        self.recreate_time = 10 * ONE_MIN  # recreate every 10min

    def __repr__(self):
        return 'mysql: connect at: 3306'


class MemcachedUnAuth(VulDocker):
    def __init__(self):
        super().__init__()
        self.name = 'memcached_unauth'
        self.docker_image = 'memcached:latest'
        self.ports = {'11211': 11211}
        self.recreate_time = ONE_HOUR  # every 10min

    def __repr__(self):
        return "memcached unauth service at 11211"


class SQLInjLib(VulDocker):
    def __init__(self):
        super().__init__()
        self.name = 'sqlinj-lib'
        self.docker_image = 'tuxotron/audi_sqli'
        self.ports = {'80/tcp': 9201}
        self.recreate_time = 24 * ONE_HOUR  # every hour

    def __repr__(self):
        return "SQL injlib from https://github.com/Audi-1/sqli-labs. visit: 9201"


class FakeWebApp(VulDocker):
    def __init__(self):
        super().__init__()
        self.name = 'fake_web_app'
        self.docker_image = 'imfht/vuln_web'
        self.recreate_time = 1 * ONE_HOUR
        self.network_mode = "host"

    def __repr__(self):
        return "A honeyport still from IPv4 space."


vuls = [DVWA(), SSHFakePass(), FTPFakePass(), RedisUnAuth(), MysqlFakePass(), MemcachedUnAuth(), SQLInjLib(),
        FakeWebApp()]
