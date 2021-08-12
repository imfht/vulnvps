from vulns.util import ONE_MIN, ONE_HOUR
from . import VulDocker


class RedisUnAuth(VulDocker):
    def __init__(self):
        super().__init__()
        self.name = 'redis-unauth'
        self.docker_image = 'redis:latest'
        self.ports = {'6379/tcp': 6379}
        self.recreate_time = 10 * ONE_MIN  # 10 min

    def __repr__(self):
        return "一个未授权的Redis服务。"


class MemcachedUnAuth(VulDocker):
    def __init__(self):
        super().__init__()
        self.name = 'memcached_unauth'
        self.docker_image = 'memcached:latest'
        self.ports = {'11211': 11211}
        self.recreate_time = ONE_HOUR  # every 10min

    def __repr__(self):
        return "一个未授权的memcached服务。"


class MongoUnauth(VulDocker):
    def __init__(self):
        super().__init__()
        self.name = "mongo_unauth"
        self.docker_image = "mongo:3"
        self.recreate_time = ONE_HOUR
        self.ports = {'27017/tcp': 27017}

    def __repr__(self):
        return "一个未授权的MongoDB服务."


class MysqlFakePass(VulDocker):
    def __init__(self):
        super().__init__()
        self.name = 'mysql_fake_pass'
        self.docker_image = 'mysql:5'
        self.environment = {'MYSQL_ROOT_PASSWORD': 'root'}
        self.ports = {'3306': 3306}
        self.recreate_time = 10 * ONE_MIN  # recreate every 10min

    def __repr__(self):
        return '一个弱口令MySQL服务'


class PostgresqlUnauth(VulDocker):
    def __init__(self):
        super().__init__()
        self.name = "postgres_fake_pass"
        self.docker_image = "postgres:9"
        self.recreate_time = ONE_HOUR
        self.ports = {'5432': 5432}

    def __repr__(self):
        return "一个未授权的postgres服务."
