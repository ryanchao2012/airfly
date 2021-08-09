# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.models.baseoperator import BaseOperator


class CloudDLPCancelDLPJobOperator(BaseOperator):
    dlp_job_id: "str"
    project_id: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPCreateDeidentifyTemplateOperator(BaseOperator):
    organization_id: "typing.Union[str, NoneType]"
    project_id: "typing.Union[str, NoneType]"
    deidentify_template: "typing.Union[typing.Dict, google.cloud.dlp_v2.types.DeidentifyTemplate, NoneType]"
    template_id: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPCreateDLPJobOperator(BaseOperator):
    project_id: "typing.Union[str, NoneType]"
    inspect_job: "typing.Union[typing.Dict, google.cloud.dlp_v2.types.InspectJobConfig, NoneType]"
    risk_job: "typing.Union[typing.Dict, google.cloud.dlp_v2.types.RiskAnalysisJobConfig, NoneType]"
    job_id: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    wait_until_finished: "bool"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPCreateInspectTemplateOperator(BaseOperator):
    organization_id: "typing.Union[str, NoneType]"
    project_id: "typing.Union[str, NoneType]"
    inspect_template: "typing.Union[google.cloud.dlp_v2.types.InspectTemplate, NoneType]"
    template_id: "typing.Union[typing.Dict, google.cloud.dlp_v2.types.InspectTemplate, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPCreateJobTriggerOperator(BaseOperator):
    project_id: "typing.Union[str, NoneType]"
    job_trigger: "typing.Union[typing.Dict, google.cloud.dlp_v2.types.JobTrigger, NoneType]"
    trigger_id: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPCreateStoredInfoTypeOperator(BaseOperator):
    organization_id: "typing.Union[str, NoneType]"
    project_id: "typing.Union[str, NoneType]"
    config: "typing.Union[google.cloud.dlp_v2.types.StoredInfoTypeConfig, NoneType]"
    stored_info_type_id: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPDeidentifyContentOperator(BaseOperator):
    project_id: "typing.Union[str, NoneType]"
    deidentify_config: "typing.Union[typing.Dict, google.cloud.dlp_v2.types.DeidentifyConfig, NoneType]"
    inspect_config: "typing.Union[typing.Dict, google.cloud.dlp_v2.types.InspectConfig, NoneType]"
    item: "typing.Union[typing.Dict, google.cloud.dlp_v2.types.ContentItem, NoneType]"
    inspect_template_name: "typing.Union[str, NoneType]"
    deidentify_template_name: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPDeleteDeidentifyTemplateOperator(BaseOperator):
    template_id: "str"
    organization_id: "typing.Union[str, NoneType]"
    project_id: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPDeleteDLPJobOperator(BaseOperator):
    dlp_job_id: "str"
    project_id: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPDeleteInspectTemplateOperator(BaseOperator):
    template_id: "str"
    organization_id: "typing.Union[str, NoneType]"
    project_id: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPDeleteJobTriggerOperator(BaseOperator):
    job_trigger_id: "str"
    project_id: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPDeleteStoredInfoTypeOperator(BaseOperator):
    stored_info_type_id: "str"
    organization_id: "typing.Union[str, NoneType]"
    project_id: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPGetDeidentifyTemplateOperator(BaseOperator):
    template_id: "str"
    organization_id: "typing.Union[str, NoneType]"
    project_id: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPGetDLPJobOperator(BaseOperator):
    dlp_job_id: "str"
    project_id: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPGetDLPJobTriggerOperator(BaseOperator):
    job_trigger_id: "str"
    project_id: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPGetInspectTemplateOperator(BaseOperator):
    template_id: "str"
    organization_id: "typing.Union[str, NoneType]"
    project_id: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPGetStoredInfoTypeOperator(BaseOperator):
    stored_info_type_id: "str"
    organization_id: "typing.Union[str, NoneType]"
    project_id: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPInspectContentOperator(BaseOperator):
    project_id: "typing.Union[str, NoneType]"
    inspect_config: "typing.Union[typing.Dict, google.cloud.dlp_v2.types.InspectConfig, NoneType]"
    item: "typing.Union[typing.Dict, google.cloud.dlp_v2.types.ContentItem, NoneType]"
    inspect_template_name: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPListDeidentifyTemplatesOperator(BaseOperator):
    organization_id: "typing.Union[str, NoneType]"
    project_id: "typing.Union[str, NoneType]"
    page_size: "typing.Union[int, NoneType]"
    order_by: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPListDLPJobsOperator(BaseOperator):
    project_id: "typing.Union[str, NoneType]"
    results_filter: "typing.Union[str, NoneType]"
    page_size: "typing.Union[int, NoneType]"
    job_type: "typing.Union[str, NoneType]"
    order_by: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPListInfoTypesOperator(BaseOperator):
    language_code: "typing.Union[str, NoneType]"
    results_filter: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPListInspectTemplatesOperator(BaseOperator):
    organization_id: "typing.Union[str, NoneType]"
    project_id: "typing.Union[str, NoneType]"
    page_size: "typing.Union[int, NoneType]"
    order_by: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPListJobTriggersOperator(BaseOperator):
    project_id: "typing.Union[str, NoneType]"
    page_size: "typing.Union[int, NoneType]"
    order_by: "typing.Union[str, NoneType]"
    results_filter: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPListStoredInfoTypesOperator(BaseOperator):
    organization_id: "typing.Union[str, NoneType]"
    project_id: "typing.Union[str, NoneType]"
    page_size: "typing.Union[int, NoneType]"
    order_by: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPRedactImageOperator(BaseOperator):
    project_id: "typing.Union[str, NoneType]"
    inspect_config: "typing.Union[typing.Dict, google.cloud.dlp_v2.types.InspectConfig, NoneType]"
    image_redaction_configs: "typing.Union[typing.Dict, google.cloud.dlp_v2.proto.dlp_pb2.ImageRedactionConfig, NoneType]"
    include_findings: "typing.Union[bool, NoneType]"
    byte_item: "typing.Union[typing.Dict, google.cloud.dlp_v2.types.ByteContentItem, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPReidentifyContentOperator(BaseOperator):
    project_id: "typing.Union[str, NoneType]"
    reidentify_config: "typing.Union[typing.Dict, google.cloud.dlp_v2.types.DeidentifyConfig, NoneType]"
    inspect_config: "typing.Union[typing.Dict, google.cloud.dlp_v2.types.InspectConfig, NoneType]"
    item: "typing.Union[typing.Dict, google.cloud.dlp_v2.types.ContentItem, NoneType]"
    inspect_template_name: "typing.Union[str, NoneType]"
    reidentify_template_name: "typing.Union[str, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPUpdateDeidentifyTemplateOperator(BaseOperator):
    template_id: "str"
    organization_id: "typing.Union[str, NoneType]"
    project_id: "typing.Union[str, NoneType]"
    deidentify_template: "typing.Union[typing.Dict, google.cloud.dlp_v2.types.DeidentifyTemplate, NoneType]"
    update_mask: "typing.Union[typing.Dict, google.protobuf.field_mask_pb2.FieldMask, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPUpdateInspectTemplateOperator(BaseOperator):
    template_id: "str"
    organization_id: "typing.Union[str, NoneType]"
    project_id: "typing.Union[str, NoneType]"
    inspect_template: "typing.Union[typing.Dict, google.cloud.dlp_v2.types.InspectTemplate, NoneType]"
    update_mask: "typing.Union[typing.Dict, google.protobuf.field_mask_pb2.FieldMask, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPUpdateJobTriggerOperator(BaseOperator):
    job_trigger_id: "_empty"
    project_id: "typing.Union[str, NoneType]"
    job_trigger: "typing.Union[google.cloud.dlp_v2.types.JobTrigger, NoneType]"
    update_mask: "typing.Union[typing.Dict, google.protobuf.field_mask_pb2.FieldMask, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"


class CloudDLPUpdateStoredInfoTypeOperator(BaseOperator):
    stored_info_type_id: "_empty"
    organization_id: "typing.Union[str, NoneType]"
    project_id: "typing.Union[str, NoneType]"
    config: "typing.Union[typing.Dict, google.cloud.dlp_v2.types.StoredInfoTypeConfig, NoneType]"
    update_mask: "typing.Union[typing.Dict, google.protobuf.field_mask_pb2.FieldMask, NoneType]"
    retry: "typing.Union[google.api_core.retry.Retry, NoneType]"
    timeout: "typing.Union[float, NoneType]"
    metadata: "typing.Union[typing.Sequence[typing.Tuple[str, str]], NoneType]"
    gcp_conn_id: "str"
    impersonation_chain: "typing.Union[str, typing.Sequence[str], NoneType]"
