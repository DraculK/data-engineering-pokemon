from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from main import check_if_data_exists, set_unique_id

default_args = {
    'owner': 'poke',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}


with DAG(
    default_args=default_args,
    dag_id='poke_crawler',
    description='Dag to crawl pokemon data',
    start_date=datetime(2024, 1, 4),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='Data_Validation',
        python_callable=check_if_data_exists,
        op_args=['dags/poke.json']
    )

    task2 = PythonOperator(
        task_id='Unique_ID',
        python_callable=set_unique_id,
        op_args=['poke.csv']

    )
    task1 >> task2
