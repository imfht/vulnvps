from vulns import VulDocker
from vulns.util import ONE_MIN, ONE_HOUR


class SSHFakePass(VulDocker):
    def __init__(self, **kwargs):
        super().__init__()
        self.name = 'ssh-fake-pass'
        self.docker_image = 'arvindr226/alpine-ssh:latest'
        self.ports = {'22/tcp': 2222}
        self.recreate_time = 2 * ONE_MIN  # rebuild every two minute.

    def __repr__(self):
        return "一个真实的ssh弱口令环境。root/root"


class FTPFakePass(VulDocker):
    def __init__(self, **kwargs):
        super().__init__()
        self.name = 'ftp-fake-pass'
        self.docker_image = 'fauria/vsftpd:latest'
        self.ports = {'21/tcp': 21, '20/tcp': 20}
        self.recreate_time = 60 * 60  # rebuild every hour.
        self.environment = {'FTP_USER': 'test', 'FTP_PASS': '123456'}

    def __repr__(self):
        return '一个真实的FTP弱口令环境。test:123456'


class RDPY(VulDocker):
    def __init__(self, **kwargs):
        super().__init__()
        self.name = "rdp"
        self.docker_image = "dtagdevsec/rdpy:1903"
        self.ports = {"3389/tcp": 3389}
        self.recreate_time = ONE_HOUR  # rebuild every hour.

    def __repr__(self):
        return "一个开放的rdp服务"
