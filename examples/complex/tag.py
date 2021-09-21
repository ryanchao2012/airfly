from airfly.model.airflow import AirflowTask

from .entry import create_entry_gcs, delete_entry_group


# Create
class create_tag(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo create_tag")


class create_tag_result(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo create_tag_result")
    upstreams = create_tag


class create_tag_result2(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo create_tag_result2")
    upstreams = create_tag


class create_tag_template(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo create_tag_template")
    upstreams = create_entry_gcs


class create_tag_template_result(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo create_tag_template_result")
    upstreams = create_tag_template


class create_tag_template_result2(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo create_tag_template_result2")
    upstreams = create_tag_template


class create_tag_template_field(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo create_tag_template_field")
    upstreams = create_tag_template


class create_tag_template_field_result(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo create_tag_template_field_result")
    upstreams = create_tag_template_field


class create_tag_template_field_result2(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo create_tag_template_field_result2")
    upstreams = create_tag_template_field


# Delete
class delete_tag(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo delete_tag")

    upstreams = create_tag


class delete_tag_template_field(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo delete_tag_template_field")

    upstreams = (create_tag_template, create_tag_template_field, delete_tag)


class delete_tag_template(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo delete_tag_template")

    upstreams = delete_tag_template_field
    downstreams = delete_entry_group


# Get
class get_tag_template(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo get_tag_template")
    upstreams = create_tag_template
    downstreams = delete_tag_template


class get_tag_template_result(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo get_tag_template_result")
    upstreams = get_tag_template


# List
class list_tags(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo list_tags")
    upstreams = create_tag
    downstreams = delete_tag


class list_tags_result(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo list_tags_result")
    upstreams = list_tags


# Rename
class rename_tag_template_field(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo rename_tag_template_field")
    upstreams = create_tag_template_field
    downstreams = delete_tag_template_field


# Update
class update_tag(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo update_tag")
    upstreams = create_tag
    downstreams = delete_tag


class update_tag_template(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo update_tag_template")
    upstreams = create_tag_template
    downstreams = delete_tag_template


class update_tag_template_field(AirflowTask):
    operator_class = "BashOperator"
    params = dict(bash_command="echo update_tag_template_field")
    upstreams = create_tag_template_field
    downstreams = rename_tag_template_field
