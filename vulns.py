import time

import docker
import schedule
from loguru import logger

from vulns import *


class DockerMonitor:
    def __init__(self):
        self.docker = docker.from_env()
        self.vuls = vuls
        self.logger = logger
        self.scheduler = schedule

    def start(self):
        self._pull_all_images()
        for vul in self.vuls:
            self.recreate_vul_docker(vul)
            self.scheduler.every(vul.recreate_time).seconds.do(self.recreate_vul_docker, vul=vul)
        while True:
            schedule.run_pending()
            self.logger.debug("docker monitor is running.")
            time.sleep(1)

    def _pull_all_images(self):
        for vul in self.vuls:
            self.logger.debug("pulling image: %s" % vul.docker_image)
            self.docker.images.pull(vul.docker_image)
            self.logger.debug("pulled image: %s" % vul.docker_image)

    def _delete_docker(self, vul):
        try:
            container = self.docker.containers.get(vul.name)
            if container:
                container.remove(force=True)
        except Exception as e:
            self.logger.warning("remove error: %s" % e)
        self.logger.info("removed %s" % vul.name)

    def _create_docker(self, vul):
        """
        :type vul: DVWA
        """
        self.logger.debug("trying to start %s" % vul.name)
        self.docker.containers.run(vul.docker_image, remove=True, detach=True, ports=vul.ports, name=vul.name,
                                   environment=vul.__dict__.get('environment'))
        self.logger.info("started %s" % vul.name)

    def recreate_vul_docker(self, vul):
        self._delete_docker(vul)
        self._create_docker(vul)


if __name__ == '__main__':
    DockerMonitor().start()
