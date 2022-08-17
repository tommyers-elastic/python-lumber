# Python lumberjack client test

To run logstash locally:

```bash
docker run --rm -it -p5044:5044 docker.elastic.co/logstash/logstash:8.3.3
```

To run the test app: 

```bash
python -m venv env 
env/bin/pip install -e ../../
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
