import requests, json

baseURI = 'https://petstore.swagger.io/v2/pet/'
petId = '192'

# /pet/{petId}
# Testing valid response or response is not empty
def test_getPetById_response():
    url = baseURI + petId
    headers = {'Content-Type': 'application/json'}
    print("RequestURL: ", url)

    response = requests.get(url, verify=False, headers=headers)
    # verify => to check servers TLS certificate
    data = response.json()
    print(json.dumps(data, indent=3))

    assert len(data) > 0, "empty response"


# Test response body for "ID" key
def test_getPetById_checkID():
    url = baseURI + petId
    headers = {'Content-Type': 'application/json'}
    print("RequestURL: ", url)

    response = requests.get(url, verify=False, headers=headers)
    data = response.json()

    assert data['id'] == 21


# Test adding new pet to store
def test_addNewPet():
    url = baseURI
    headers = {'Content-Type': 'application/json'}
    payload = {
                  "id": petId,
                  "category": {
                    "id": 0,
                    "name": "string"
                  },
                  "name": "JenyFur",
                  "photoUrls": [
                    "string"
                  ],
                  "tags": [
                    {
                      "id": 0,
                      "name": "string"
                    }
                  ],
                  "status": "available"
                }
    response = requests.post(url, verify=False, json=payload, headers=headers)
    data = response.json()
    assert len(data) > 0
    assert data['id'] == 192, "New pet created successfully!"
    print(json.dumps(data, indent=3))