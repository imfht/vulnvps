import signal
import sys

import click
import docker
import schedule

from vulns import *


class DockerMonitor:
    def __init__(self, force_pull):
        self.docker = docker.from_env()
        self.vuls = vuls
        self.logger = logger
        self.scheduler = schedule
        self.force_pull = force_pull
        signal.signal(signal.SIGINT, self.signal_handler)

    def start(self):
        if self.force_pull:
            self._pull_all_images()
        for vul in self.vuls:
            self.recreate_vul_docker(vul)
            self.scheduler.every(vul.recreate_time).seconds.do(self.recreate_vul_docker, vul=vul)
        while True:
            schedule.run_pending()
            time.sleep(5)

    def _pull_all_images(self):
        for vul in self.vuls:
            self.logger.debug("start pulling image: %s" % vul.docker_image)
            self.docker.images.pull(vul.docker_image)
            self.logger.debug("finished image: %s" % vul.docker_image)

    def _delete_docker(self, vul):
        with suppress(Exception):
            self.docker.containers.get(vul.name).remove(force=True, v=True, link=True)

    def _create_container(self, vul):
        """
        :type vul: DVWA
        """
        self.docker.containers.run(vul.docker_image, remove=True, detach=True, ports=vul.ports, name=vul.name,
                                   environment=vul.__dict__.get('environment'))

        vul.init_docker()

    def recreate_vul_docker(self, vul):
        self._delete_docker(vul)
        self._create_container(vul)
        self.logger.info("recreated %s" % vul.name)

    def signal_handler(self, sig, frame):
        self.logger.info('Exiting....')
        for vul in self.vuls:
            self._delete_docker(vul)
            self.logger.info("delete %s" % vul.name)
        self.logger.info('Bye!')
        sys.exit(0)


@click.command()
@click.option('-p', default=False, help='force pull image.', is_flag=True)
def main(pull):
    """Simple program that greets NAME for a total of COUNT times."""
    DockerMonitor(force_pull=pull).start()


if __name__ == '__main__':
    main()
