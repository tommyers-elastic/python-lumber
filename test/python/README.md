# Python lumberjack client test

To generate SSL keys and certificates (one-time only):

```bash
docker run --rm -v $(pwd)/conf:/conf elasticsearch:8.3.3 bash -c \
"bin/elasticsearch-certutil cert --name localhost --self-signed --pem -out cert.zip && unzip cert.zip && \
openssl pkcs8 -topk8 -nocrypt -inform PEM -outform PEM -in localhost/localhost.key -out localhost/localhost.pkcs8.key && \
mkdir -p /conf/ssl && cp localhost/* /conf/ssl"
```

To run logstash locally, run the following command from this directory:

```bash
docker run --rm -it --name logstash -p5043:5043 -p5044:5044 -e XPACK_MONITORING_ENABLED=false \
-v $(pwd)/conf/pipeline:/usr/share/logstash/pipeline \
-v $(pwd)/conf/ssl:/usr/share/logstash/ssl \
docker.elastic.co/logstash/logstash:8.3.3
```

To run the test app: 

```bash
python -m venv env 
env/bin/pip install -e ../..\[dev]
env/bin/python test.py
```

Expected test output:
```
logstash acknowledged 4 events
```

Expected logstash output:
```
{
          "tags" => [
        [0] "beats_input_raw_event"
    ],
    "@timestamp" => 2022-08-17T22:01:25.369845Z,
      "@version" => "1",
          "name" => "edo"
}
{
          "tags" => [
        [0] "beats_input_raw_event"
    ],
    "@timestamp" => 2022-08-17T22:01:25.370028Z,
      "@version" => "1",
          "name" => "mario"
}
{
          "tags" => [
        [0] "beats_input_raw_event"
    ],
    "@timestamp" => 2022-08-17T22:01:25.369703Z,
      "@version" => "1",
          "name" => "tom"
}
{
          "tags" => [
        [0] "beats_input_raw_event"
    ],
    "@timestamp" => 2022-08-17T22:01:25.369923Z,
      "@version" => "1",
          "name" => "kaiyan"
}
```
