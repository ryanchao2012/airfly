from airfly.model import AirFly

from .entry import create_entry_gcs, delete_entry_group


# Create
class create_tag(AirFly):
    op_class = "BashOperator"
    op_params = dict(bash_command="echo create_tag")


class create_tag_result(AirFly):
    op_class = "BashOperator"
    op_params = dict(bash_command="echo create_tag_result")
    upstream = create_tag


class create_tag_result2(AirFly):
    op_class = "BashOperator"
    op_params = dict(bash_command="echo create_tag_result2")
    upstream = create_tag


class create_tag_template(AirFly):
    op_class = "BashOperator"
    op_params = dict(bash_command="echo create_tag_template")
    upstream = create_entry_gcs


class create_tag_template_result(AirFly):
    op_class = "BashOperator"
    op_params = dict(bash_command="echo create_tag_template_result")
    upstream = create_tag_template


class create_tag_template_result2(AirFly):
    op_class = "BashOperator"
    op_params = dict(bash_command="echo create_tag_template_result2")
    upstream = create_tag_template


class create_tag_template_field(AirFly):
    op_class = "BashOperator"
    op_params = dict(bash_command="echo create_tag_template_field")
    upstream = create_tag_template


class create_tag_template_field_result(AirFly):
    op_class = "BashOperator"
    op_params = dict(bash_command="echo create_tag_template_field_result")
    upstream = create_tag_template_field


class create_tag_template_field_result2(AirFly):
    op_class = "BashOperator"
    op_params = dict(bash_command="echo create_tag_template_field_result2")
    upstream = create_tag_template_field


# Delete
class delete_tag(AirFly):
    op_class = "BashOperator"
    op_params = dict(bash_command="echo delete_tag")

    upstream = create_tag


class delete_tag_template_field(AirFly):
    op_class = "BashOperator"
    op_params = dict(bash_command="echo delete_tag_template_field")

    upstream = (create_tag_template, create_tag_template_field, delete_tag)


class delete_tag_template(AirFly):
    op_class = "BashOperator"
    op_params = dict(bash_command="echo delete_tag_template")

    upstream = delete_tag_template_field
    downstream = delete_entry_group


# Get
class get_tag_template(AirFly):
    op_class = "BashOperator"
    op_params = dict(bash_command="echo get_tag_template")
    upstream = create_tag_template
    downstream = delete_tag_template


class get_tag_template_result(AirFly):
    op_class = "BashOperator"
    op_params = dict(bash_command="echo get_tag_template_result")
    upstream = get_tag_template


# List
class list_tags(AirFly):
    op_class = "BashOperator"
    op_params = dict(bash_command="echo list_tags")
    upstream = create_tag
    downstream = delete_tag


class list_tags_result(AirFly):
    op_class = "BashOperator"
    op_params = dict(bash_command="echo list_tags_result")
    upstream = list_tags


# Rename
class rename_tag_template_field(AirFly):
    op_class = "BashOperator"
    op_params = dict(bash_command="echo rename_tag_template_field")
    upstream = create_tag_template_field
    downstream = delete_tag_template_field


# Update
class update_tag(AirFly):
    op_class = "BashOperator"
    op_params = dict(bash_command="echo update_tag")
    upstream = create_tag
    downstream = delete_tag


class update_tag_template(AirFly):
    op_class = "BashOperator"
    op_params = dict(bash_command="echo update_tag_template")
    upstream = create_tag_template
    downstream = delete_tag_template


class update_tag_template_field(AirFly):
    op_class = "BashOperator"
    op_params = dict(bash_command="echo update_tag_template_field")
    upstream = create_tag_template_field
    downstream = rename_tag_template_field
