from datetime import datetime

from airflow import DAG, macros
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
with DAG(dag_id="macro_example", schedule_interval="*/10 * * * *", default_args=default_args) as dag:
    t1 = BashOperator(
    task_id="display",
    bash_command="echo 'execution date : {{ ds }} modified by macros.ds_add to add 5 days : {{ macros.ds_add(ds, 5) }}'"
    )
    t1

