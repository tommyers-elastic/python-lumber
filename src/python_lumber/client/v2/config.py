from os import access, R_OK
from os.path import isfile


class ConfigError(Exception):
    pass


class ClientConfig:
    def __init__(
        self,
        connection_timeout_s=None,
        read_timeout_s=None,
        write_timeout_s=None,
        compression_level=0,
        cert_file=None,
    ):
        self.connection_timeout_s = connection_timeout_s
        self.read_timeout_s = read_timeout_s
        self.write_timeout_s = write_timeout_s
        self.compression_level = compression_level
        self.cert_file = cert_file

    def validate(self):
        if self.connection_timeout_s is not None and self.connection_timeout_s <= 0:
            raise ConfigError('connection timeout must be a positive number')

        if self.read_timeout_s is not None and self.read_timeout_s <= 0:
            raise ConfigError('read timeout must be a positive number')

        if self.write_timeout_s is not None and self.write_timeout_s <= 0:
            raise ConfigError('write timeout must be a positive number')

        if self.compression_level not in range(0, 10):
            raise ConfigError('compression level must be in range 0-9')

        if self.cert_file is not None and not self._check_file(self.cert_file):
            raise ConfigError('invalid SSL certificate file')

        return self

    @staticmethod
    def _check_file(f):
        return isfile(f) and access(f, R_OK)
