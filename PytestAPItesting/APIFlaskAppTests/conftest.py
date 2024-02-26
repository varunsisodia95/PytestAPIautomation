import pytest
from utils.fileUtils import getJsonFromFile
from utils.apiUtils import getApiData, postApiData
from utils.myconfigparser import getFlaskAppBaseURL

loginJsonFile = 'loginValid.json'
baseURI = getFlaskAppBaseURL()
loginURLPath = 'login'


@pytest.fixture
def get_token():
    url = baseURI + loginURLPath
    payload = getJsonFromFile(loginJsonFile)
    resp = postApiData(url, payload)
    print(resp.json()['token'])
    token = resp.json()['token']
    yield token