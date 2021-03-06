# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class CloudSQLBaseOperator(BaseOperator):
    instance: "str"
    project_id: "typing.Union[str, NoneType]"
    gcp_conn_id: "str"
    api_version: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudSQLCreateInstanceDatabaseOperator(CloudSQLBaseOperator):
    instance: "str"
    body: "dict"
    project_id: "typing.Union[str, NoneType]"
    gcp_conn_id: "str"
    api_version: "str"
    validate_body: "bool"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudSQLCreateInstanceOperator(CloudSQLBaseOperator):
    body: "dict"
    instance: "str"
    project_id: "typing.Union[str, NoneType]"
    gcp_conn_id: "str"
    api_version: "str"
    validate_body: "bool"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudSQLDeleteInstanceDatabaseOperator(CloudSQLBaseOperator):
    instance: "str"
    database: "str"
    project_id: "typing.Union[str, NoneType]"
    gcp_conn_id: "str"
    api_version: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudSQLDeleteInstanceOperator(CloudSQLBaseOperator):
    instance: "str"
    project_id: "typing.Union[str, NoneType]"
    gcp_conn_id: "str"
    api_version: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudSQLExecuteQueryOperator(BaseOperator):
    sql: "typing.Union[typing.List[str], str]"
    autocommit: "bool"
    parameters: "typing.Union[typing.Dict, typing.Iterable, NoneType]"
    gcp_conn_id: "str"
    gcp_cloudsql_conn_id: "str"


class CloudSQLExportInstanceOperator(CloudSQLBaseOperator):
    instance: "str"
    body: "dict"
    project_id: "typing.Union[str, NoneType]"
    gcp_conn_id: "str"
    api_version: "str"
    validate_body: "bool"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudSQLImportInstanceOperator(CloudSQLBaseOperator):
    instance: "str"
    body: "dict"
    project_id: "typing.Union[str, NoneType]"
    gcp_conn_id: "str"
    api_version: "str"
    validate_body: "bool"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudSQLInstancePatchOperator(CloudSQLBaseOperator):
    body: "dict"
    instance: "str"
    project_id: "typing.Union[str, NoneType]"
    gcp_conn_id: "str"
    api_version: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudSQLPatchInstanceDatabaseOperator(CloudSQLBaseOperator):
    instance: "str"
    database: "str"
    body: "dict"
    project_id: "typing.Union[str, NoneType]"
    gcp_conn_id: "str"
    api_version: "str"
    validate_body: "bool"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"
