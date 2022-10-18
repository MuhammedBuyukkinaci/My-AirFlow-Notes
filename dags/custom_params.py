from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
"owner": "Airflow",
"start_date": datetime(2019, 7, 29),
"depends_on_past": False,
"email_on_failure": False,
"email_on_retry": False,
"email": "youremail@host.com",
"retries": 1
}

with DAG(dag_id="custom_params", schedule_interval="*/10 * * * *", default_args=default_args) as dag:
    t1 = BashOperator(
    task_id="display",
    bash_command="echo {{ params.my_param }}",
    params={"my_param": "Hello world"}
    )
    t1
