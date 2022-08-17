from python_lumber.client.v2 import Client
from python_lumber.client.v2 import ClientConfig


client = Client(ClientConfig(
    **{
        'connection_timeout_s': 1,
        'read_timeout_s': 1, 
        'write_timeout_s': 1,
        'compression_level': 9,
    }
))
client.connect('localhost:5044')

data = [
    {'name': 'tom'},
    {'name': 'edo'},
    {'name': 'kaiyan'},
    {'name': 'mario'},
]
client.send(data)
read = client.ack(len(data))

print(f'logstash acknowledged {read} events')

client.close()
