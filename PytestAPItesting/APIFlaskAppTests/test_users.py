import json
import pytest

from utils.fileUtils import getJsonFromFile
from utils.apiUtils import getApiData, postApiData
from utils.myconfigparser import getFlaskAppBaseURL

baseURI = getFlaskAppBaseURL()
usersUrlPath = 'users'


# Test get users with fixtures
def test_getUsers(get_token):
    token = get_token
    userURL = baseURI + usersUrlPath
    headers = {'x-access-token': token}
    resp_users = getApiData(userURL, opHeader=headers)
    print(json.dumps(resp_users.json(), indent=4))
    assert resp_users.json()['users'][0]['email']
