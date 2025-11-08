from __future__ import annotations

import logging
import sys
import time
from pprint import pprint

import pendulum

from airflow import DAG
from airflow.decorators import dag, task
from airflow.operators.python import is_venv_installed

log = logging.getLogger(__name__)

PATH_TO_PYTHON_BINARY = sys.executable

with DAG(
    dag_id="dags_python_task_decorator",
    schedule="0 2 * * 1",
    start_date=pendulum.datetime(2024, 1, 1, tz="UTC"),
    catchup=False,
) as dag:
    
    @task(task_id="python_task_1")
    def print_context(some_input):
        print(some_input)
        
    python_task_1 = print_context('task_decorator 실행')