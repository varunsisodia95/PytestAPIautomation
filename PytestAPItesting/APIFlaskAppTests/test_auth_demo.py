from utils.fileUtils import getJsonFromFile
from utils.apiUtils import getApiData, postApiData
from utils.myconfigparser import getFlaskAppBaseURL

loginJsonFile = 'loginValid.json'
baseURI = getFlaskAppBaseURL()
loginURLPath = 'login'
usersUrlPath = 'users'


def test_getUserDemo():
    loginUrl = baseURI + loginURLPath
    payload = getJsonFromFile(loginJsonFile)
    resp = postApiData(loginUrl, payload)
    print(resp.json()['token'])
    token = resp.json()['token']

    usrURL = baseURI + usersUrlPath
    headers = {'x-access-token': token}
    resp_users = getApiData(usrURL, opHeader=headers)
    print(resp_users.json())





