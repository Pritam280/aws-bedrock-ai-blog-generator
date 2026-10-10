# AWS Bedrock AI Blog Generator

An AI-powered web application that generates blog content from user-provided topics using Amazon Bedrock and Meta Llama 3.1 8B Instruct.

## Project Overview

This project demonstrates how to build and deploy a serverless AI application on AWS. Users enter a topic through a web interface, the backend invokes a foundation model, and the generated blog is stored in Amazon S3.

## Architecture

**Flow:** User → Amazon S3 Static Website → Amazon API Gateway → AWS Lambda → Amazon Bedrock → AWS Lambda → Amazon S3

## AWS Services Used

* **Amazon Bedrock:** Generates blog content using Meta Llama 3.1 8B Instruct.
* **AWS Lambda:** Processes requests and invokes the foundation model.
* **Amazon API Gateway:** Exposes the backend through an HTTP API.
* **Amazon S3:** Hosts the frontend and stores generated blog files.
* **AWS IAM:** Controls permissions between AWS services.
* **Amazon CloudWatch:** Supports logging and troubleshooting.

## Features

* Generate blog content from a user-provided topic.
* Integrate a web frontend with a serverless backend.
* Invoke a foundation model through Amazon Bedrock.
* Save generated blog output in Amazon S3.
* Handle API errors and display status messages.

## Repository Structure

* `frontend/` — Web application.
* `lambda/` — Backend Lambda function.
* `architecture/` — System architecture diagram.
* `screenshots/` — Application and AWS console screenshots.

## Deployment Overview

1. Create an Amazon S3 bucket to host the frontend.
2. Deploy the Lambda function with the required IAM permissions.
3. Configure Amazon Bedrock model access.
4. Create an HTTP API in API Gateway and integrate it with Lambda.
5. Configure CORS for the frontend origin.
6. Upload the frontend to S3 and test blog generation.
7. Verify that generated blog files are stored in S3.

## Security Considerations

* Use least-privilege IAM permissions.
* Never commit AWS access keys, secret keys, account credentials, or sensitive environment variables.
* Restrict public access to generated content unless public sharing is explicitly required.
* Review API access controls and monitor costs.

## Future Improvements

* Infrastructure as Code using Terraform.
* CI/CD deployment using GitHub Actions.
* Authentication and request throttling.
* CloudWatch alarms and cost monitoring.
* Automated tests for the Lambda function.

## Author

Cloud and DevOps learning project.
