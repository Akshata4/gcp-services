from google.cloud import bigquery

# Initialize client
client = bigquery.Client(project=project_id)

# Configure load job
job_config = bigquery.LoadJobConfig(
    source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
    autodetect=True,  # Let BigQuery detect schema automatically
    write_disposition=bigquery.WriteDisposition.WRITE_APPEND
)

# Execute load job
with open(json_file_path, "rb") as source_file:
    job = client.load_table_from_file(
        source_file,
        destination=f"{project_id}.{dataset_id}.{table_id}",
        job_config=job_config
    )

job.result()  # Wait for job completion

print(f"Loaded {job.output_rows} rows to {dataset_id}.{table_id}")
