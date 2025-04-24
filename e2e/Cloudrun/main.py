from flask import Flask, request
import os

from lib.read_from_gcs.read_gcs_file_as_json as read_gcs_file_as_json


app = Flask(__name__)

@app.route('/read_file', methods=['POST'])
def read_file():
    request_data = request.get_json()
    filename = request_data.get("filename")
    filepath = request_data.get("filepath")
    project = request_data.get("project")

    bucket_name = filepath.split('/')[0]
    blob_ame = '/'.join(filepath.split('/')[0])+filename
    ## read data from GCS bucket
    data = read_gcs_file_as_json(bucket_name, blob_name)
    

    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
