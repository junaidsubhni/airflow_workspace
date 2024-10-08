from datetime import datetime

from airflow.models import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator

with DAG(
        dag_id="00_launch",
        start_date=datetime(year=2019, month=1, day=1),
        end_date=datetime(year=2019, month=1, day=5),
        schedule="@daily",
):
    prm = EmptyOperator(task_id="procure_rocket_material")

    pf = EmptyOperator(task_id="procure_fuel")

    build1 = EmptyOperator(task_id="build_stage_1")

    build2 = EmptyOperator(task_id="build_stage_2")

    build3 = EmptyOperator(task_id="build_stage_3")

    launch = EmptyOperator(task_id="launch")


    prm >> [build1, build2, build3] >> launch
    pf >> build3 >> launch
