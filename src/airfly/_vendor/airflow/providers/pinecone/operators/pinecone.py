# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class PineconeIngestOperator(BaseOperator):
    conn_id: "str"
    index_name: "str"
    input_vectors: "list[tuple]"
    namespace: "str"
    batch_size: "int | None"
    upsert_kwargs: "dict | None"
