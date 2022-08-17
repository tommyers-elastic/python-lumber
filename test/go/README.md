# Golang lumberjack client test

To run logstash locally:

```bash
docker run --rm -it -p5044:5044 docker.elastic.co/logstash/logstash:8.3.3
```

To run the test app: 

```bash
go run .
```

Expected test output:
```
logstash acknowledged 5 events
```

Expected logstash output:
```
{
    "@timestamp" => 2022-08-17T14:17:17.105730Z,
          "Name" => "dan",
      "@version" => "1",
          "tags" => [
        [0] "beats_input_raw_event"
    ]
}
{
    "@timestamp" => 2022-08-17T14:17:17.105501Z,
          "Name" => "tom",
      "@version" => "1",
          "tags" => [
        [0] "beats_input_raw_event"
    ]
}
{
    "@timestamp" => 2022-08-17T14:17:17.106077Z,
          "Name" => "davide",
      "@version" => "1",
          "tags" => [
        [0] "beats_input_raw_event"
    ]
}
{
    "@timestamp" => 2022-08-17T14:17:17.105976Z,
          "Name" => "mario",
      "@version" => "1",
          "tags" => [
        [0] "beats_input_raw_event"
    ]
}
{
    "@timestamp" => 2022-08-17T14:17:17.105869Z,
          "Name" => "kaiyan",
      "@version" => "1",
          "tags" => [
        [0] "beats_input_raw_event"
    ]
}
```
