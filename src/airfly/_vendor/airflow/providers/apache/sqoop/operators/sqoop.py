# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class SqoopOperator(BaseOperator):
    conn_id: "str"
    cmd_type: "str"
    table: "typing.Union[str, NoneType]"
    query: "typing.Union[str, NoneType]"
    target_dir: "typing.Union[str, NoneType]"
    append: "bool"
    file_type: "str"
    columns: "typing.Union[str, NoneType]"
    num_mappers: "typing.Union[int, NoneType]"
    split_by: "typing.Union[str, NoneType]"
    where: "typing.Union[str, NoneType]"
    export_dir: "typing.Union[str, NoneType]"
    input_null_string: "typing.Union[str, NoneType]"
    input_null_non_string: "typing.Union[str, NoneType]"
    staging_table: "typing.Union[str, NoneType]"
    clear_staging_table: "bool"
    enclosed_by: "typing.Union[str, NoneType]"
    escaped_by: "typing.Union[str, NoneType]"
    input_fields_terminated_by: "typing.Union[str, NoneType]"
    input_lines_terminated_by: "typing.Union[str, NoneType]"
    input_optionally_enclosed_by: "typing.Union[str, NoneType]"
    batch: "bool"
    direct: "bool"
    driver: "typing.Union[typing.Any, NoneType]"
    verbose: "bool"
    relaxed_isolation: "bool"
    properties: "typing.Union[typing.Dict[str, typing.Any], NoneType]"
    hcatalog_database: "typing.Union[str, NoneType]"
    hcatalog_table: "typing.Union[str, NoneType]"
    create_hcatalog_table: "bool"
    extra_import_options: "typing.Union[typing.Dict[str, typing.Any], NoneType]"
    extra_export_options: "typing.Union[typing.Dict[str, typing.Any], NoneType]"
