import random
import time

import pytest
from utils.apiUtils import postApiData, delApiData
from utils.fileUtils import getJsonFromFile
from utils.myconfigparser import getFlaskAppBaseURL

baseURI = getFlaskAppBaseURL()
regUrlPath = 'register'
loginUrlPath = 'login'
delUrlPath = 'delete'
registerJSONFile = 'registerApiValid.json'
randNum = random.randint(0, 1000)
email = 'automateuser@auto' + str(randNum)
password = '1234'


def getPayloadDict_regApi(email=None, pwd=None):
    payload = getJsonFromFile(registerJSONFile)
    payload['email'] = email
    payload['password'] = pwd
    return payload


@pytest.fixture(scope='module')
def reg_user():
    print("Inside fixture setup")
    payload = getPayloadDict_regApi(email, password)
    regUrl = baseURI + regUrlPath
    reg_resp = postApiData(regUrl, payload)
    assert reg_resp.status_code == 201
    assert reg_resp.json()['id']
    data = reg_resp.json()
    yield data # Anything after this will run as part of teardown or after the test is executed
    time.sleep(5)
    print("Inside fixture teardown")
    delUrl = baseURI + delUrlPath
    loginUrl = baseURI + loginUrlPath
    login_resp = postApiData(loginUrl, payload)
    token = login_resp.json()['token']

    headers = {'x-access-token': token}
    payload = {'id': reg_resp.json()['id']}
    del_resp = delApiData(delUrl, payload, headers)
    assert del_resp.status_code == 200
    assert del_resp.json()['id'] == reg_resp.json()['id']


def test_loginCorrectCreds(reg_user):
    payload = getPayloadDict_regApi(email, password)
    url = baseURI + loginUrlPath
    resp = postApiData(url, payload)
    assert resp.status_code == 200


def test_loginEmptyPassword(reg_user):
    payload = getPayloadDict_regApi(email, '')
    url = baseURI + loginUrlPath
    resp = postApiData(url, payload)
    assert resp.status_code == 401






