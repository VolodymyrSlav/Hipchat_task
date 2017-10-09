# Hipchat_task
RESTful API that takes a chat message string as input and returns a JSON object containing information about its contents. There are also 3 tests for proper work of all supported input values.

Installation
------------
There are some packages that should be installed:
* Python-2.7.5
* pytets-3.2.3
* py-1.4.34
* pluggy-0.4.0
* gunicorn 19.7.1

Quickstart
----------
1. Change directory right to hipchat folder
2. Use command ``` pip install –r requirements.txt ``` to set dependencies
3. Use command ``` ginicorn api:api ``` to run application(this will run server on port 8000)
4. Send request by bash script to see the output. For expample, curl_req.sh or your own curl request.
5. Use command ```pytest tests``` to run 3 tests(mentions, emoticons, links)
