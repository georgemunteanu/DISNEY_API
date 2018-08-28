Task DISNEY - API testing
----------


## Overview:
The tests will exercise DISNEY - API for:
- posting new post
- deleting new post
- duplicate username
Processing will be done by "requests" python library.
Assertion will be done with python core unittest framework.
Reporting - the test will outpout a xml report.


## Pre-requisites:
'''   - python 3.6.x
   - pip install requests
   - pip install xmlrunner   '''


## Structure:
- sources: http methods, http request elements, http response elements
- runner: test health check api, end-2-end tests



## Run tests locally:
   - go to $/api_functionality/sources
   - execute "test_end_2_end.py" -> it will output a xml report



## Run health check:
   - go to $/api_test
   - execute "test_health_check_api.py" -> it will output a MessageBox




----------
End of document
