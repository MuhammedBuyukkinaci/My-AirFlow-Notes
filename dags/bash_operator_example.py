from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy_operator import DummyOperator

with DAG(dag_id='bash_dag_with_jinja', schedule_interval="@once", start_date=datetime(2020, 1, 1), catchup=False) as dag:
    # Task 1
    dummy_task = DummyOperator(task_id='dummy_task')
    # Task 2
    commands = """
        mkdir -p /usr/local/airflow/dags/{{ ds }};
        cp /usr/local/airflow/dags/command.sh /usr/local/airflow/dags/{{ ds }};
        sh /usr/local/airflow/dags/{{ ds }}/command.sh;
        """
    bash_task = BashOperator(task_id='bash_task', bash_command=commands)
    dummy_task >> bash_task
