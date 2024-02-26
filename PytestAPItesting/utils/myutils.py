import requests, json


# Create new pet using POST
def postAPIdata(url, payload):
    headers = {'Content-Type': 'application/json'}
    print('Request URL: ', url)
    response = requests.post(url=url, json=payload, verify=False, headers=headers)
    data = response.json()
    print(data)

    return data, response.status_code, response.elapsed.total_seconds()


# Returns API response data
def getAPIdata(url):
    headers = {'Content-Type': 'application/json'}
    print('Request URL: ', url)
    response = requests.get(url, verify=False, headers=headers)
    data = response.json()
    assert len(data) > 0, "empty response"
    return data, response.status_code, response.elapsed.total_seconds()


# Put API call
def putData(url, body):
    headers = {'Content-Type': 'application/json'}
    print('Request URL: ', url)
    print("ReqBody: ", json.dumps(body))
    response = requests.put(url, verify=False, json=body, headers=headers)
    data = response.json()
    timetaken = response.elapsed.total_seconds()
    return data, response.status_code, timetaken


# Delete API call
def deleteData(url):
    headers = {'Content-Type': 'application/json'}
    print('Request URL: ', url)

    # Value when true ==> if condition
    # Value when false ==> else condition
    response = requests.delete(url, verify=False, headers=headers)
    print(response.request.headers)

    data = response.json()
    timeTaken = response.elapsed.total_seconds()
    return data, response.status_code, timeTaken




