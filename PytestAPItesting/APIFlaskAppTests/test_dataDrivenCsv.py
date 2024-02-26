import pytest

from utils.fileUtils import getCsvDataAsDict,getDataAsTuple
from utils.apiUtils import postApiData
from utils.myconfigparser import getFlaskAppBaseURL

baseURI = getFlaskAppBaseURL()
dataFile = 'D:\\PytestAPItesting\\TestData\\resgisterAPIdata.csv'
urlPath = 'register'
dataFileWithStatus = 'D:\\PytestAPItesting\\TestData\\registerApiDataWithStatus.csv'
getData = getDataAsTuple(dataFileWithStatus)


def test_datadrivenRegAPI():
    url = baseURI + urlPath
    payloadList = getCsvDataAsDict(dataFile)

    for datalines in payloadList:
        print(datalines)
        resp = postApiData(url, datalines)
        assert resp.status_code == 201
        data = resp.json()
        print(data)
        assert data['id']


@pytest.mark.parametrize("input, respStatus", getData)
def test_dataDrivenParameterized(input, respStatus):
    url = baseURI + urlPath
    keys = ['email', 'password']
    requestDict = dict(zip(keys, input))
    print("Request dict: "+str(requestDict), str(respStatus))
    resp = postApiData(url, requestDict)
    assert resp.status_code == int(respStatus)











