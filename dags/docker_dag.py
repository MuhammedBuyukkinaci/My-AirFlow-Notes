from datetime import datetime
from sys import api_version

from airflow.decorators import dag, task
from airflow.providers.docker.operators.docker import DockerOperator


@dag(start_date= datetime(2021,1,1), schedule_interval='@daily', catchup=False)
def docker_dag():

    @task
    def t1():
        pass

    t2 = DockerOperator(
        task_id = 't2',
        api_version = 'auto',
        container_name = 'task_t2',
        image = 'python:3.8-slim-buster',
        command = 'echo "command running in the docker container" ',
        docker_url = 'unix://var/run/docker.sock',
        network_mode = 'bridge',#really common
        xcom_all = True,
        retrieve_output = True,
        retrieve_output_path = '/tmp/script.out',
        mem_limit = '512m',
        auto_remove = True,
        mount_tmp_dir = False,
        cpus = 2
        #mounts = []

    )

    t1() >> t2


dag = docker_dag()
