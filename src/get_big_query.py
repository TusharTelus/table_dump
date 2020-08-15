from google.cloud import bigquery
from logger.log import logger
project_id = "biquery-286107"
client = bigquery.Client(project_id)



def create_data_Set(data_set_name):
    dataset_id = project_id +"."+ data_set_name
    dataset = bigquery.Dataset(dataset_id)
    return dataset.dataset_id


def create_schema(dataset_id, table_id):
    table_id = project_id +"."+dataset_id+"."+table_id
    schema = [
        bigquery.SchemaField("name", "STRING", mode="REQUIRED"),
        bigquery.SchemaField("age", "INTEGER", mode="REQUIRED"),]
    table = bigquery.Table(table_id, schema=schema)
    table = client.create_table(table)  # Make an API request.
    table_id = f"{table.project_id}.{table.dataset_id}.{table.table_id}"
    return table_id

def upload_csv(table_id):
    job_config = bigquery.LoadJobConfig(
             source_format = bigquery.SourceFormat.CSV, skip_leading_rows = 1, autodetect = True,
                                                                                                 )
    job_config.write_disposition = 'WRITE_APPEND'
    job_config.schemaUpdateOptions = ['ALLOW_FIELD_ADDITION', 'ALLOW_FIELD_RELAXATION']
    with open("interview.csv", "rb") as source_file:
        job = client.load_table_from_file(source_file, table_id, job_config=job_config)
    job.result()  # Waits for the job to complete.
    table = client.get_table(table_id)  # Make an API request.
    logger.info(
       "Loaded {} rows and {} columns to {}".format(
             table.num_rows, len(table.schema), table_id
       ))




