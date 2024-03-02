import os
import pathlib
import uuid


def from_url_wrapper(url):
    pool = redis.ConnectionPool.from_url(url)
    return redis.Redis.from_pool(pool)


class Config:
    DEFAULT_CONFIG_PATH = '/tmp/asgilook'
    DEFAULT_MIN_THUMB_SIZE = 64
    DEFAULT_REDIS_HOST = 'redis://localhost'
    DEFAULT_UUID_GENERATOR = uuid.uuid4
    DEFAULT_REDIS_FROM_URL = from_url_wrapper

    def __init__(self):
        self.storage_path = pathlib.Path(
            os.environ.get('ASGI_LOOK_STORAGE_PATH', self.DEFAULT_CONFIG_PATH)
        )
        self.storage_path.mkdir(parents=True, exist_ok=True)

        self.min_thumb_size = self.DEFAULT_MIN_THUMB_SIZE
        self.redis_from_url = Config.DEFAULT_REDIS_FROM_URL
        self.redis_host = self.DEFAULT_REDIS_HOST
        self.uuid_generator = Config.DEFAULT_UUID_GENERATOR
