from datetime import datetime, timedelta

from airflow.models import DAG
from airflow.operators.empty import EmptyOperator

with DAG(
        dag_id="02_exercise",
        start_date=datetime(year=2024, month=9, day=1),
        end_date=datetime(year=2024, month=10, day=15),
        schedule=timedelta(days=3),
):
    prm = EmptyOperator(task_id="procure_rocket_material")

    pf = EmptyOperator(task_id="procure_fuel")

    build1 = EmptyOperator(task_id="build_stage_1")

    build2 = EmptyOperator(task_id="build_stage_2")

    build3 = EmptyOperator(task_id="build_stage_3")

    launch = EmptyOperator(task_id="launch")


    prm >> [build1, build2, build3] >> launch
    pf >> build3 >> launch
