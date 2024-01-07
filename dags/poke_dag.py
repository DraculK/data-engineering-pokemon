from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from main import check_if_data_exists

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
        task_id='PokeSpider',
        python_callable=check_if_data_exists,
        op_args=['dags/poke.json']
    )
    task1
