from airflow.sdk import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime

def print_context(**context): # Added ** to handle the context dictionary
    print(context)

# 1. Added a start_date (required for the scheduler)
# 2. Added a schedule (optional, None means manual trigger)
dag = DAG(
    dag_id="my_first_dag",
    start_date=datetime(2026, 1, 23), 
    schedule="@daily",
    catchup=True, 
)

task = PythonOperator(
    task_id="my_first_task",
    python_callable=print_context,
    dag=dag,
)
