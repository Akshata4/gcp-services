# Hello World Cloud Run Service

## Overview

This is a simple Python Flask app that responds with **"Hello, World!"** to HTTP requests at the root path.

## Features

- Responds with `"Hello, World!"` at the root URL (`/`).

## Deploying to Google Cloud Run

You can deploy this app directly from source using the Google Cloud CLI:

`gcloud run deploy hello-world-service --source .`


Follow the prompts to select your region and allow unauthenticated access.

After deployment, Cloud Run will provide a public URL for your service. Visit this URL in your browser or use `curl` to test:

`curl http://127.0.0.1:8080/`


## Running Locally

To run the app locally on port 8080:

`python main.py`


---

## Additional Information

Cloud Run is a fully managed serverless platform by Google Cloud that lets you deploy containerized applications easily without managing infrastructure.

