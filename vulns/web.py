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
        self.recreate_time = ONE_HOUR  # will 'never' recreate dvwa for some reason.

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


class SQLInjLib(VulDocker):
    def __init__(self):
        super().__init__()
        self.name = 'sqlinj-lib'
        self.docker_image = 'tuxotron/audi_sqli'
        self.ports = {'80/tcp': 9201}
        self.recreate_time = 24 * ONE_HOUR  # every hour

    def __repr__(self):
        return "SQL injlib at: 9201"


class FakeWebApp(VulDocker):
    def __init__(self):
        super().__init__()
        self.name = 'fake_web_app'
        self.docker_image = 'imfht/vuln_web'
        self.recreate_time = 1 * ONE_DAY
        self.network_mode = "host"

    def __repr__(self):
        return "A honeyport still from IPv4 space."
