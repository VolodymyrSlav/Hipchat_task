import falcon
from falcon import testing
import json
import pytest
from hipchat.api import api

@pytest.fixture
def client():
    return testing.TestClient(api)

def test_links(client):
    params = {"input": "Have you ever visited http://atlassian.com and http://google.com.ua"}
    doc = {
        "links": [ { "url": "http://atlassian.com", "title": "Atlassian | Software Development and Collaboration Tools"}, 
	 {"url": "http://google.com.ua", "title": "Google"} ]
    }

    response = client.simulate_get('/', params=params)

    assert response.content == json.dumps(doc)
    assert response.status == falcon.HTTP_OK

