import zlib
from . import protocol
import socket
import ujson


class Client:
    def __init__(self, config):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.config = config.validate()

    def connect(self, address):
        host, port = address.split(':')
        self.sock.settimeout(self.config.connection_timeout_s)
        self.sock.connect((host, int(port)))
    
    def close(self):
        self.sock.close()

    def send(self, messages):
        if len(messages) == 0:
            return 

        payload = bytearray()

        payload.extend(protocol.CODE_VERSION)
        payload.extend(protocol.CODE_WINDOW_SIZE)
        payload.extend(self._format_int(len(messages)))

        message_frames = self._serialize(messages)

        if self.config.compression_level > 0:
            payload.extend(protocol.CODE_VERSION)
            payload.extend(protocol.CODE_COMPRESSED)
            compressed_frames = zlib.compress(message_frames, self.config.compression_level)
            payload.extend(self._format_int(len(compressed_frames)))
            payload.extend(compressed_frames)
        else:
            payload.extend(message_frames)

        self.sock.settimeout(self.config.write_timeout_s)
        self.sock.sendall(payload)

    def ack(self, message_count): 
        ack_seq = 0
        while ack_seq < message_count:
            ack_seq = self._recv_ack()
        
        if ack_seq > message_count:
            raise protocol.ProtocolError(f'invalid ack sequence number received; expected {message_count}, got {ack_seq}')

        return ack_seq

    def _recv_ack(self):
        self.sock.settimeout(self.config.read_timeout_s)
        with self.sock.makefile() as s:
            msg = s.read(6).encode('utf-8')
        
        if msg[0:1] != protocol.CODE_VERSION or msg[1:2] != protocol.CODE_ACK:
            raise protocol.ProtocolError('invalid ack response')
        
        return int.from_bytes(msg[2:], byteorder='big')

    @classmethod
    def _serialize(cls, messages):
        data = bytearray()
        for i, item in enumerate(messages):
            encoded = ujson.dumps(item).encode('utf-8')

            data.extend(protocol.CODE_VERSION)
            data.extend(protocol.CODE_JSON_DATA_FRAME)
            data.extend(cls._format_int(i + 1))
            data.extend(cls._format_int(len(encoded)))
            data.extend(encoded)

        return data

    @staticmethod
    def _format_int(i):
        # fixme: handle ints that are too big?
        return int(i).to_bytes(4, byteorder='big')