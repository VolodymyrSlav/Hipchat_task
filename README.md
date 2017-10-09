# Hipchat_task
RESTful API that takes a chat message string as input and returns a JSON object containing information about its contents. There are also 3 tests for proper work of all supported input values.


Quickstart
----------
1. Use command ``` pip install –r requirements.txt ``` to set dependencies
2. Use command ``` ginicorn api:api ``` to run application(this will run server on port 8000)
3. Send request by bash script to see the output. For expample, curl_req.sh or your own curl request.
4. Use command ```pytest tests``` to run 3 tests(mentions, emoticons, links)

Expample of request
-------------------

```curl -G http://localhost:8000/ --data-urlencode "input=Hipchat is (awesome) application developed by (smart) @john and @tom from http://www.atlassian.com and is definitelly better than http://www.slack.com" | jq ```

