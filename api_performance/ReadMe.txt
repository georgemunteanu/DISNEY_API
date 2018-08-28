Task DISNEY  - API Performance
----------


## Overview:
The tests will exercise DISNEY - API for performance for:
- GET "/version"
Processing and assertion will be done by "locustio" python library.
Reporting - the test will outpout a html report.


## Pre-requisites:
   - python 3.6.x
   - pip install locustio  (read also: https://docs.locust.io)



## Structure:
- sources: runner.py



## Run tests locally:
   - go to $/api_performance
   - open a cmd
   - type: "locust -f runner.py --host=http://localhost:9000"
   - then go to: http://localhost:8089/ and enter "user" and click "swarming" > the report is shown in real-time 







----------
End of document
