import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

url = 'https://httpbin.org/basic-auth/abc/abc'
auth = HTTPDigestAuth('abc', 'abc')


# Basic authentication
def test_basicAuth():
    headers = {'Accept':'application/json'}
    r = requests.get(url, auth=auth, verify=False)
    print(r.status_code)


