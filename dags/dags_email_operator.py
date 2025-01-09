from airflow import DAG
import datetime
import pendulum
from airflow.operators.email import EmailOperator

# catchup: 누락되어 있는 작업을 진행을 할 것인가 결정 -> true일 경우 차례차례 돌리는게 아니라 한번에 돌린다.
# 객체id와 task id는 같게 가져가는 표준으로 가겠다.

with DAG(
    dag_id="dags_email_operator",
    schedule="30 9 15-21 * 5#3",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    send_email_task = EmailOperator(
        task_id='send_email_task',
        to='nekote4@naver.com',
        subject='오늘은 가정의날 입니다!!',
        html_content='''
            <h2>Airflow Success Mail</h2>
            <br>
            Airflow 작업이 완료되었습니다.
        '''
    )
