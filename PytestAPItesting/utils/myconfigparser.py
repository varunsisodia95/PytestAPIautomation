import configparser
from pathlib import Path

cfgFile = 'petsqa.ini'
cfgFileDir = 'config'

cfgFileFlaskApp = 'qa.ini'

config = configparser.ConfigParser()
configForFlask = configparser.ConfigParser()

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)

CONFIG_FILE = BASE_DIR.joinpath(cfgFileDir).joinpath(cfgFile)
CONFIG_FILE_FLASKAPP = BASE_DIR.joinpath(cfgFileDir).joinpath(cfgFileFlaskApp)

config.read(CONFIG_FILE)
configForFlask.read(CONFIG_FILE_FLASKAPP)

def getFlaskAppBaseURL():
    baseURL = 'http://' + configForFlask['flaskapp']['url'] + ":" + configForFlask['flaskapp']['port'] + '/api/'
    return baseURL

def getPetAPIUrl():
    return config['pet']['url']


def getStoreAPIUrl():
    return config['store']['url']

print(getFlaskAppBaseURL())
print(getPetAPIUrl())
print(getStoreAPIUrl())



