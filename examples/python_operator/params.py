from datetime import datetime

dag_kwargs = dict(
    schedule_interval=None,
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["example"],
)
