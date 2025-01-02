import random
import pendulum

from airflow import DAG
from airflow.operators.python import PythonOperator

from common.common_func import regist

# catchup: 누락되어 있는 작업을 진행을 할 것인가 결정 -> true일 경우 차례차례 돌리는게 아니라 한번에 돌린다.
# 객체id와 task id는 같게 가져가는 표준으로 가겠다.

with DAG(
    dag_id="dags_python_with_op_args",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:

    regist_t1 = PythonOperator(
        task_id='regist_t1',
        python_callable=regist,
        op_args=['bcshin','man','kr','seoul']
    )

    regist_t1
