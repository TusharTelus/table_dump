from google.cloud import bigquery
client = bigquery.Client("biquery-286107")

def create_dataset(table_name):
    table_id = "biquery-286107.abcdp" + "table_name"
    job_config = bigquery.LoadJobConfig(
        schema=[
            bigquery.SchemaField("name", "STRING"),
            bigquery.SchemaField("post_abbr", "STRING"),
        ],
        skip_leading_rows=1,

        source_format=bigquery.SourceFormat.CSV,
    )
    uri = "gs://cloud-samples-data/bigquery/us-states/us-states.csv"

    load_job = client.load_table_from_uri(
        uri, table_id, job_config=job_config
    )

    load_job.result()

    destination_table = client.get_table(table_id)
    return True
