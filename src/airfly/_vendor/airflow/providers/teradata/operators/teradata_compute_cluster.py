# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class _TeradataComputeClusterOperator(BaseOperator):
    compute_profile_name: "str"
    compute_group_name: "str | None"
    teradata_conn_id: "str"
    timeout: "int"


class TeradataComputeClusterProvisionOperator(_TeradataComputeClusterOperator):
    query_strategy: "str | None"
    compute_map: "str | None"
    compute_attribute: "str | None"


class TeradataComputeClusterDecommissionOperator(_TeradataComputeClusterOperator):
    delete_compute_group: "bool"


class TeradataComputeClusterResumeOperator(_TeradataComputeClusterOperator):
    pass


class TeradataComputeClusterSuspendOperator(_TeradataComputeClusterOperator):
    pass
