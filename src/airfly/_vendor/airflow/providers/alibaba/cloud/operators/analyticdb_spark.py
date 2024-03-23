# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class AnalyticDBSparkBaseOperator(BaseOperator):
    adb_spark_conn_id: "str"
    region: "str | None"
    polling_interval: "int"


class AnalyticDBSparkSQLOperator(AnalyticDBSparkBaseOperator):
    sql: "str"
    conf: "dict[Any, Any] | None"
    driver_resource_spec: "str | None"
    executor_resource_spec: "str | None"
    num_executors: "int | str | None"
    name: "str | None"
    cluster_id: "str"
    rg_name: "str"


class AnalyticDBSparkBatchOperator(AnalyticDBSparkBaseOperator):
    file: "str"
    class_name: "str | None"
    args: "Sequence[str | int | float] | None"
    conf: "dict[Any, Any] | None"
    jars: "Sequence[str] | None"
    py_files: "Sequence[str] | None"
    files: "Sequence[str] | None"
    driver_resource_spec: "str | None"
    executor_resource_spec: "str | None"
    num_executors: "int | str | None"
    archives: "Sequence[str] | None"
    name: "str | None"
    cluster_id: "str"
    rg_name: "str"
