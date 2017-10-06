import falcon
from falcon import testing
import json
import pytest
from hipchat.api import api

@pytest.fixture
def client():
    return testing.TestClient(api)

def test_mentions(client):
    params = {"input": "@mike @stan where are you?"}
    doc = {
        "mentions": [ "mike", "stan" ]
    }

    response = client.simulate_get('/', params=params)

    assert response.content == json.dumps(doc)
    assert response.status == falcon.HTTP_OK

