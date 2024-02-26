from utils.apiUtils import getApiData
from utils.myconfigparser import getFlaskAppBaseURL

baseURL = getFlaskAppBaseURL()
urlPath = 'allusercount'


# Testing API user count for status 200
def test_getAlluserCountStatus200():
    url = baseURL + urlPath
    headers = {'Accept':'application/json'}
    resp = getApiData(url, headers)
    assert resp.status_code == 200


# Test for invalid header
def test_getAllUserCountStatus406():
    url = baseURL + urlPath
    headers = {'Content-Type':'application/pdf'}
    resp = getApiData(url, headers)
    assert resp.status_code == 406


# Checking response body
def test_getAllUserCountBody():
    url = baseURL + urlPath
    headers = {'Accept':'application/json'}
    resp = getApiData(url, headers)
    data = resp.json()
    assert data['count']
    assert data['status']
    assert data['status']['message'] == 'success'


# Checking response time
def test_getAllUserCountTimeTaken():
    url = baseURL + urlPath
    headers = {'Accept':'application/json'}
    resp = getApiData(url, headers)
    data = resp.json()
    print(resp.elapsed.total_seconds())
    assert (resp.elapsed.total_seconds()) < 1
