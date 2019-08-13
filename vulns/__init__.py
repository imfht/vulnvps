class DVWA:
    def __init__(self, **kwargs):
        self.name = 'dvwa'
        self.docker_image = 'imfht/dvwa-nologin'
        self.ports = {'80/tcp': 9200}
        self.recreate_time = 60 * 10  # 10min

    def __repr__(self):
        return "dvwa: visit :9200"


class SSHFakePass:
    def __init__(self, **kwargs):
        self.name = 'ssh-fake-pass'
        self.docker_image = 'arvindr226/alpine-ssh'
        self.ports = {'22/tcp': 2222}
        self.recreate_time = 60 * 2  # rebuild every two minute.

    def __repr__(self):
        return "ssh: login as root/root"


class FTPFakePass:
    def __init__(self, **kwargs):
        self.name = 'ftp-fake-pass'
        self.docker_image = 'fauria/vsftpd'
        self.ports = {'21/tcp': 21, '20/tcp': 20}
        self.recreate_time = 60 * 2  # rebuild every two minute.
        self.environment = {'FTP_USER': 'test', 'FTP_PASS': '123456'}

    def __repr__(self):
        return 'ftp: login as test:123456'


class RedisUnAuth:
    def __init__(self):
        self.name = 'redis'
        self.docker_image = 'redis'
        self.ports = {'6379/tcp': 6379}
        self.recreate_time = 60 * 10  # 10 min

    def __repr__(self):
        return "redis: connect at :6379"


class MysqlFakePass:
    def __init__(self):
        self.name = 'mysql_fake_pass'
        self.docker_image = 'mysql'
        self.environment = {'MYSQL_ROOT_PASSWORD': 'root'}
        self.ports = {'3306': 3306}
        self.recreate_time = 60 * 10  # recreate every 10min

    def __repr__(self):
        return 'mysql: connect at: 3306'


vuls = [DVWA(), SSHFakePass(), FTPFakePass(), RedisUnAuth(), MysqlFakePass()]
