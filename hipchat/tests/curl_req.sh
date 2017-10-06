#!/bin/bash
curl -G http://localhost:8000/ --data-urlencode "input=Hipchat is (awesome) application developed by (smart) @john and @tom from http://www.atlassian.com and is definitelly better than http://www.slack.com" | jq
