# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class HiveToSambaOperator(BaseOperator):
    hql: "str"
    destination_filepath: "str"
    samba_conn_id: "str"
    hiveserver2_conn_id: "str"
