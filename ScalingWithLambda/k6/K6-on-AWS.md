#1 Using K6 with AWS I used
[these instructions as a base](https://aws.plainenglish.io/load-testing-apis-with-k6-a-practical-guide-to-aws-integration-with-datadog-823b06a0a2a5)

To use [K6](https://github.com/grafana/k6) for testing you can

### Local Setup

Install on mac via `brew intstall k6`.

Reccomend you create a docker image (which you will deploy to EC2) with the tests and
depdendies installed for easy testing/reproducability.
