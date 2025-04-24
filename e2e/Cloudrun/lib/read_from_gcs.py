from google.cloud import storage
import json

def read_gcs_file_as_json(bucket_name, blob_name):
    # Initialize a GCS client (ensure your environment is authenticated)
    storage_client = storage.Client()
    
    # Get the bucket and blob (file) reference
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    
    # Download the file's contents as a string
    file_contents = blob.download_as_string()
    
    # Parse the string as JSON
    data = json.loads(file_contents)
    
    return data

# Example usage:
# data = read_gcs_file_as_json("your-bucket-name", "your-file.json")
# print(data)
