from python_lumber.client.v2 import Client

client = Client(write_timeout_s=1, read_timeout_s=1)
client.connect('localhost:5044', 1)

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
