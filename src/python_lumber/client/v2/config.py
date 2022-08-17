from multiprocessing import connection

class ConfigError(Exception): pass

class ClientConfig:
    def __init__(
        self,
        connection_timeout_s,
        read_timeout_s,
        write_timeout_s,
        compression_level,
    ):
        self.connection_timeout_s = connection_timeout_s
        self.read_timeout_s = read_timeout_s 
        self.write_timeout_s = write_timeout_s 
        self.compression_level = compression_level 
    
    def validate(self):
        if self.connection_timeout_s <= 0:
            raise ConfigError('connection timeout must be a positive number')

        if self.read_timeout_s <= 0:
            raise ConfigError('read timeout must be a positive number')

        if self.write_timeout_s <= 0:
            raise ConfigError('write timeout must be a positive number')

        if self.compression_level not in range(0, 10):
            raise ConfigError('compression level must be in range 0-9')
        
        return self