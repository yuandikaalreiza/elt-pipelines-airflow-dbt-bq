from airflow.decorators import dag, task
from datetime import datetime
from airflow.providers.google.cloud.transfers.local_to_gcs import LocalFilesystemToGCSOperator

@dag(
    start_date=datetime(2023, 1, 1),
    schedule=None,
    catchup=False,
    tags=['retail']
)

def retail():
    
    upload_csv_to_gcs = LocalFilesystemToGCSOperator(
        task_id='upload_csv_to_gcs',
        src='/usr/local/airflow/include/dataset/online_retail.csv',
        dst='raw/online_retail.csv',
        bucket='u1_elt_bucket',
        gcp_conn_id='gcp',
        mime_type='text/csv'
    )

retail()