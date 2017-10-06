import falcon
from falcon import testing
import json
import pytest
from hipchat.api import api

@pytest.fixture
def client():
    return testing.TestClient(api)

def test_emoticons(client):
    params = {"input": "I am so (glad) that I've been able to checkout HipChat - this is such an (awesome) tool"}
    doc = {
        "emoticons": [ "glad", "awesome" ]
    }

    response = client.simulate_get('/', params=params)

    assert response.content == json.dumps(doc)
    assert response.status == falcon.HTTP_OK

