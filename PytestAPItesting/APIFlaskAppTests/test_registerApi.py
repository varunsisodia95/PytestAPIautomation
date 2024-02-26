from utils.apiUtils import postApiData
from utils.fileUtils import getJsonFromFile
from utils.myconfigparser import getFlaskAppBaseURL

baseURI = getFlaskAppBaseURL()
urlPath = 'register'
registerJsonFile = 'registerApiValid.json'

# Testing register API with body from file
def test_registerAPI():
    url = baseURI + urlPath
    payload = getJsonFromFile(registerJsonFile)
    resp = postApiData(url, payload)
    print(resp.json())
    assert resp.status_code == 201



