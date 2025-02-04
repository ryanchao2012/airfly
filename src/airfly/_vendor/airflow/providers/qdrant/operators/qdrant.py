# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class QdrantIngestOperator(BaseOperator):
    conn_id: "str"
    collection_name: "str"
    vectors: "Iterable[VectorStruct]"
    payload: "Iterable[dict[str, Any]] | None"
    ids: "Iterable[int | str] | None"
    batch_size: "int"
    parallel: "int"
    method: "str | None"
    max_retries: "int"
    wait: "bool"
