package main

import (
	"fmt"
	"log"

	lumberjack "github.com/elastic/go-lumber/client/v2"
)

type Data struct {
	Name string
}

func main() {
	syncClient, err := lumberjack.SyncDial("localhost:5044")
	if err != nil {
		log.Fatalf("could not connect to logstash: %v", err)
	}
	defer syncClient.Close()

	payload := []interface{}{Data{"tom"}, Data{"dan"}, Data{"kaiyan"}, Data{"mario"}, Data{"davide"}}

	read, err := syncClient.Send(payload)
	if err != nil {
		log.Fatalf("sync send failed: %v", err)
	}

	fmt.Printf("logstash acknowledged %d events\n", read)
}
