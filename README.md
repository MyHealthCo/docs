# Docs

[![maintainer is djfurman](https://img.shields.io/badge/maintainer-djfurman-blueviolet)](https://github.com/djfurman)
[![license is BSD-3](https://img.shields.io/badge/license-BSD--3-yellow)](https://github.com/MyHealthCo/docs/blob/main/LICENSE)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-blue?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

Documents, diagrams, and findings in source format for experiments.

Disclaimer: This organization, including but not limited to its infrastructure, cloud provider setup, templates, and data are entirely fake. While efforts are made to remain true to the spirit of constraints, these experiments are just that, experiments. **Do not implement these experiment services and expect them to be compliant or cover all production hardening considerations.** They inform microservices architecture choices, nothing more.

## Purpose

Provide version controlled assumptions, design, documentation, diagrams, discussion, and findings as code in support of experiments.

MyHealthCo is a fake company with no basis on any real organization. Healthcare was chosen because

1. Standards (both US and international) mandate security practices and associated cloud design considerations
1. Healthcare encounters are common in base form and require significant amounts of complex interactions involving:
  1. personally identifiable information
  1. private information
  1. financial interactions
  1. third-party data transmissions to private industry service providers (e.g., health insurance providers, pharmacies)
  1. third-party data transmission to public/government organizations (e.g., public health organizations, public health aid programs, government health insurance)
1. Health practices can readily model microservices for real time interactions, extract-transform-load (ETL), big data, and network interactions across logically separated cloud accounts/services

Each experiment allows for exploring an area of interest within mocked meaningful constraints.

### Load Testing Cloud Cache on AWS

Identify baseline metrics between simple serverless applications using a cache fetch system comparing persistence layers between AWS DynamoDB and AWS ElasticCache using Redis.

Experiment design, methods, and findings [log and discussion](./experiments/cloud-cache-load-test.md) provides the working document.

## Contributions

All contributions are welcome. Please open an issue or PR as fit to help enhance this utility.

Experiments are just that, ideas to be tested. This documentation exists to try and call out assumptions and document problem statement, design, methods, execution, results and discussion. If you find potential special cause variation, errata or other issues, please open an issue to discuss! Iteration will only make this better.

When contributing, please install the pre-commit plugins and follow the style guide.
