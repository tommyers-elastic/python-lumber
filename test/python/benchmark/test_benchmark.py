import gzip
from os.path import abspath, dirname, join
from python_lumber.client.v2 import Client
from python_lumber.client.v2 import ClientConfig
import requests
import ujson

here = abspath(dirname(__file__))
certfile = join(here, '../conf/ssl/localhost.crt')
compression_level = 9
number_of_events_per_request = 50  # request size = approx. 874 bytes / event


def setup_data(num_records):
    with open(join(here, 'sample_data.json')) as f:
        json_content = ujson.loads(f.read())

    return [json_content] * num_records


def test_lumberjack(benchmark):
    client = Client(ClientConfig(
        **{
            'connection_timeout_s': 1,
            'read_timeout_s': 1,
            'write_timeout_s': 1,
            'compression_level': compression_level,
            'cert_file': certfile,
            'hostname': 'localhost',
        }
    ))
    client.connect('localhost:5044')

    data = setup_data(number_of_events_per_request)
    num_messages = len(data)
    assert num_messages == number_of_events_per_request

    def send():
        client.send(data)
        client.ack(num_messages)

    benchmark(send)


def test_https(benchmark):
    data = setup_data(number_of_events_per_request)
    session = requests.Session()
    session.verify = certfile

    def send():
        ndjson = '\n'.join(ujson.dumps(item) for item in data)
        session.put(
            'https://localhost:5043',
            data=gzip.compress(ndjson.encode('utf-8'), compression_level),
            headers={'Content-Encoding': 'gzip', 'Content-Type': 'application/x-ndjson'}
        )

    benchmark(send)


def test_https_no_gzip(benchmark):
    data = setup_data(number_of_events_per_request)
    session = requests.Session()
    session.verify = certfile

    def send():
        ndjson = '\n'.join(ujson.dumps(item) for item in data)
        session.put(
            'https://localhost:5043',
            data=ndjson.encode('utf-8'),
            headers={'Content-Type': 'application/x-ndjson'}
        )

    benchmark(send)
