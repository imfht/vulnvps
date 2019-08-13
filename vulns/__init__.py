class DVWA:
    def __init__(self, **kwargs):
        self.name = 'dvwa'
        self.docker_image = 'imfht/dvwa-nologin:latest'
        self.ports = {'80/tcp': 9200}
        self.recreate_time = 60 * 10  # 10min

    def __repr__(self):
        return "dvwa: visit :9200"


class SSHFakePass:
    def __init__(self, **kwargs):
        self.name = 'ssh-fake-pass'
        self.docker_image = 'arvindr226/alpine-ssh:latest'
        self.ports = {'22/tcp': 2222}
        self.recreate_time = 60 * 2  # rebuild every two minute.

    def __repr__(self):
        return "ssh: login as root/root"


class FTPFakePass:
    def __init__(self, **kwargs):
        self.name = 'ftp-fake-pass'
        self.docker_image = 'fauria/vsftpd:latest'
        self.ports = {'21/tcp': 21, '20/tcp': 20}
        self.recreate_time = 60 * 2  # rebuild every two minute.
        self.environment = {'FTP_USER': 'test', 'FTP_PASS': '123456'}

    def __repr__(self):
        return 'ftp: login as test:123456'


class RedisUnAuth:
    def __init__(self):
        self.name = 'redis-unauth'
        self.docker_image = 'redis:latest'
        self.ports = {'6379/tcp': 6379}
        self.recreate_time = 60 * 10  # 10 min

    def __repr__(self):
        return "redis: connect at :6379"


class MysqlFakePass:
    def __init__(self):
        self.name = 'mysql_fake_pass'
        self.docker_image = 'mysql:5'
        self.environment = {'MYSQL_ROOT_PASSWORD': 'root'}
        self.ports = {'3306': 3306}
        self.recreate_time = 60 * 10  # recreate every 10min

    def __repr__(self):
        return 'mysql: connect at: 3306'


class MemcachedUnAuth:
    def __init__(self):
        self.name = 'memcached_unauth'
        self.docker_image = 'memcached:latest'
        self.ports = {'11211': 11211}
        self.recreate_time = 60 * 10  # every 10min

    def __repr__(self):
        return "memcached unauth service at 11211"


class SQLInjLib:
    def __init__(self):
        self.name = 'sqlinj-lib'
        self.docker_image = 'tuxotron/audi_sqli'
        self.ports = {'9201': 80}
        self.recreate_time = 60 * 10  # every 10min

    def __repr__(self):
        return "SQL injlib from https://github.com/Audi-1/sqli-labs. visit: 9201"


vuls = [DVWA(), SSHFakePass(), FTPFakePass(), RedisUnAuth(), MysqlFakePass(), MemcachedUnAuth(), SQLInjLib()]
