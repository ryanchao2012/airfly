# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class Neo4jOperator(BaseOperator):
    sql: "str"
    neo4j_conn_id: "str"
    parameters: "Iterable | Mapping[str, Any] | None"
