
# Pytest API automation framework

This is a sample API testing framework developed using Pytest wherein we are automating some API tests for a sample endpoint.

# Structure of framework 

1. API tests folder.
2. Config folder storing .ini files
3. Reports folder storing allure reports.
4. Test data folder storing .json, .csv files.
5. Utils folder containing helper files.

# Server for testing

Server link: https://github.com/kss7/TestFrameworkApp 

Steps to execute server:
1. Activate venv if configured.
2. In the TestFrameworkApp-Main folder, execute run.py 

# Allure reporting

1. scoop install allure
2. pip install allure-pytest
3. To execute: Pytest --alluredir= <folder name>  <test suite name>
4. This will generate some random files in at <folder name>
5. Allure serve <folder name> ==> generates allure report.


