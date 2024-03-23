from airfly.model.airflow import AirflowTask


# Create
class create_entry_group(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo create_entry_group")


class create_entry_group_result(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo create_entry_group_result")
    upstream = create_entry_group


class create_entry_group_result2(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo create_entry_group_result2")
    upstream = create_entry_group


class create_entry_gcs(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo create_entry_gcs")
    upstream = create_entry_group


class create_entry_gcs_result(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo create_entry_gcs_result")
    upstream = create_entry_gcs


class create_entry_gcs_result2(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo create_entry_gcs_result")
    upstream = create_entry_gcs


# Delete
class delete_entry(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo delete_entry")

    upstream = create_entry_gcs


class delete_entry_group(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo delete_entry_group")

    upstream = create_entry_group
    downstream = delete_entry


# Get
class get_entry_group(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo get_entry_group")
    upstream = create_entry_group
    downstream = delete_entry_group


class get_entry_group_result(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo get_entry_group_result")
    upstream = get_entry_group


class get_entry(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo get_entry")
    upstream = create_entry_gcs
    downstream = delete_entry


class get_entry_result(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo get_entry_result")
    upstream = get_entry


# Lookup
class lookup_entry(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo lookup_entry")
    upstream = create_entry_gcs
    downstream = delete_entry


class lookup_entry_result(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo lookup_entry_result")
    upstream = lookup_entry


# Update
class update_entry(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo update_entry")

    upstream = create_entry_gcs
    downstream = delete_entry
