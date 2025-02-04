# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.google.cloud.operators.cloud_base import (
    GoogleCloudBaseOperator,
)


class GCSCreateBucketOperator(GoogleCloudBaseOperator):
    bucket_name: "str"
    resource: "dict | None"
    storage_class: "str"
    location: "str"
    project_id: "str"
    labels: "dict | None"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class GCSDeleteBucketOperator(GoogleCloudBaseOperator):
    bucket_name: "str"
    force: "bool"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"
    user_project: "str | None"


class GCSListObjectsOperator(GoogleCloudBaseOperator):
    bucket: "str"
    prefix: "str | list[str] | None"
    delimiter: "str | None"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"
    match_glob: "str | None"


class GCSDeleteObjectsOperator(GoogleCloudBaseOperator):
    bucket_name: "str"
    objects: "list[str] | None"
    prefix: "str | list[str] | None"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class GCSBucketCreateAclEntryOperator(GoogleCloudBaseOperator):
    bucket: "str"
    entity: "str"
    role: "str"
    user_project: "str | None"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class GCSObjectCreateAclEntryOperator(GoogleCloudBaseOperator):
    bucket: "str"
    object_name: "str"
    entity: "str"
    role: "str"
    generation: "int | None"
    user_project: "str | None"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class GCSFileTransformOperator(GoogleCloudBaseOperator):
    source_bucket: "str"
    source_object: "str"
    transform_script: "str | list[str]"
    destination_bucket: "str | None"
    destination_object: "str | None"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"


class GCSTimeSpanFileTransformOperator(GoogleCloudBaseOperator):
    source_bucket: "str"
    source_prefix: "str"
    source_gcp_conn_id: "str"
    destination_bucket: "str"
    destination_prefix: "str"
    destination_gcp_conn_id: "str"
    transform_script: "str | list[str]"
    source_impersonation_chain: "str | Sequence[str] | None"
    destination_impersonation_chain: "str | Sequence[str] | None"
    chunk_size: "int | None"
    download_continue_on_fail: "bool | None"
    download_num_attempts: "int"
    upload_continue_on_fail: "bool | None"
    upload_num_attempts: "int"


class GCSSynchronizeBucketsOperator(GoogleCloudBaseOperator):
    source_bucket: "str"
    destination_bucket: "str"
    source_object: "str | None"
    destination_object: "str | None"
    recursive: "bool"
    delete_extra_files: "bool"
    allow_overwrite: "bool"
    gcp_conn_id: "str"
    impersonation_chain: "str | Sequence[str] | None"
