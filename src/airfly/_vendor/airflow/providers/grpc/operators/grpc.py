# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class GrpcOperator(BaseOperator):
    stub_class: "Callable"
    call_func: "str"
    grpc_conn_id: "str"
    data: "dict | None"
    interceptors: "list[Callable] | None"
    custom_connection_func: "Callable | None"
    streaming: "bool"
    response_callback: "Callable | None"
    log_response: "bool"
