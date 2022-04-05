# CloudStoreAPI
Media Storage API - Flask Microservice deployed in Cloud Run

NOTE: At the core of this API, Signing of V4 URLs is implemented to allow unauthenticated access to store, delete, get and list the media. Since it is still at nascent stage, API cannot handle the Size Chunking for resumable upload. Further iterations will include this functionality.

Before deploying the Cloud Run Application, make sure you have configured the Bucket requirements: 
  1. CORS policy of GCP bucket. If intended to be used locally for testing, this is not required.
  2. Service Account Credential File - Make sure to put all the contents of your credentials file are inside the "credentials.json". It is intended to be used when Signing V4 URLs for bucket.
