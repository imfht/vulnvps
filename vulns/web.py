import time
from contextlib import suppress

import requests
from loguru import logger

from vulns import VulDocker
from vulns.util import ONE_HOUR, ONE_DAY


class DVWA(VulDocker):
    def __init__(self, **kwargs):
        super().__init__()
        self.name = 'dvwa'
        self.docker_image = 'imfht/dvwa-nologin:latest'
        self.ports = {'80/tcp': 9200}
        self.recreate_time = ONE_DAY * 100  # will 'never' recreate dvwa for some reason.

    def __repr__(self):
        return "dvwa是一个用来进行安全脆弱性鉴定的PHP/MySQL Web应用。"

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


class Wavsep(VulDocker):
    def __init__(self):
        super().__init__()
        self.name = "wavsep"
        self.docker_image = 'imfht/wavsep'
        self.ports = {'8080/tcp': 8080}
        self.receate_time = ONE_DAY * 100

    def __repr__(self):
        return "WAVSEP 是一个包含漏洞的web应用程序，目的是帮助测试web应用漏洞扫描器的功能、质量和准确性。"


class OwaspBenchMark(VulDocker):
    def __init__(self):
        super().__init__()
        self.name = 'owasp benchmark'
        self.docker_image = 'owasp/benchmark'
        self.ports = {'8080/tcp': 8443}
        self.receate_time = ONE_DAY * 100

    def __repr__(self):
        return "OWASP benchmark是OWASP组织下的一个开源项目，又叫作OWASP基准测试项目，它是免费且开放的测试套件。 " \
               "它可以用来评估那些自动化安全扫描工具的速度、覆盖范围和准确性。"
