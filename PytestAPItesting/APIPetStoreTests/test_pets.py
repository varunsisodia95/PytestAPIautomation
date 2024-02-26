from utils.myutils import *
from utils.myconfigparser import *
import logging
LOGGER = logging.getLogger(__name__) # Good practice


baseURI = getPetAPIUrl()
petId = '1945'
petName = 'Jennyfur'
newPetDict = {
  "id": int(petId),
  "name": petName,
  "status": "available"
}


def test_postPetById():
    url = baseURI
    data, statuscode, timetaken = postAPIdata(url, newPetDict)
    LOGGER.info("New pet created successfully!")

    print(timetaken)
    assert statuscode == 200, "Pet created successfully!"
    assert data['id'] == int(petId)
    assert data['name'] == petName

def test_getPetById_response():
    url = baseURI + petId
    data, statuscode, timetaken = getAPIdata(url)
    LOGGER.info("Get message done!")
    assert statuscode == 200
    print(timetaken)
    assert data['id'] == int(petId)


# Testing update function
def test_updatePet():
    payload = {'id':int(petId), 'name':"Cutie", 'status':"pending"}
    data, resp_status, timetaken = putData(baseURI, payload)
    assert data['id'] == int(petId)
    assert resp_status == 200


def test_deletePetbyId():
    url = baseURI + petId
    data, status, timeElapsed = deleteData(url)
    print(data)
    assert data['message'] == petId
    assert data['code'] == 200
