import pytest
from utils.apiUtils import getApiData
from utils.myconfigparser import getFlaskAppBaseURL

baseURL = getFlaskAppBaseURL()
urlPath = 'allusercount'

testData = [
    ('application/json', 200),
    ('application/xml', 406),
    ('multipart/mixed', 406),
    ('text/html', 406)
]


@pytest.mark.parametrize("datatype, status", testData)
def test_getAllUserCountStatus(datatype, status):
    url = baseURL + urlPath
    headers = {'Accept': datatype}
    resp = getApiData(url, headers)
    print(resp.status_code)
    assert resp.status_code == status




