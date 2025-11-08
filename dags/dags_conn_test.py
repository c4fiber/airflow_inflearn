import pendulum
from airflow import DAG
from airflow.operators.empty import EmptyOperator

# catchup: 누락되어 있는 작업을 진행을 할 것인가 결정 -> true일 경우 차례차례 돌리는게 아니라 한번에 돌린다.
# 객체id와 task id는 같게 가져가는 표준으로 가겠다.

with DAG(
    dag_id="dags_conn_test",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    t1 = EmptyOperator(
        task_id="t1",
    )
    t2 = EmptyOperator(
        task_id="t2",
    )

    t3 = EmptyOperator(
        task_id="t3",
    )

    t4 = EmptyOperator(
        task_id="t4",
    )

    t5 = EmptyOperator(
        task_id="t5",
    )

    t6 = EmptyOperator(
        task_id="t6",
    )

    t7 = EmptyOperator(
        task_id="t7",
    )

    t8 = EmptyOperator(
        task_id="t8",
    )

    t1 >> [t2, t3] >> t4
    t5 >> t4
    [t4, t7] >> t6 >> t8
