import requests, json


def getApiData(url, opHeader=None):
    if opHeader is None:
        headers = {'Accept':'application/json'}
    else:
        headers = dict(opHeader)

    response = requests.get(url, verify=False, headers=headers)

    print("\nRequest URL: "+str(url))
    print("Request header: "+str(response.request.headers))
    print("Response header: "+str(response.headers))

    return response


def postApiData(url, body):
    headers = {'Content-Type':'application/json'}
    print("\nReq url: "+str(url))
    print("ReqBody: "+json.dumps(body))

    return requests.post(url, verify=False, json=body, headers=headers)


def delApiData(url, body, opHeader=None):
    if opHeader is None:
        headers = {'Accept':'application/json'}
    else:
        headers = dict(opHeader)
    print("\nReq url: " + str(url))
    response = requests.delete(url, json=body, headers=headers)
    return response















