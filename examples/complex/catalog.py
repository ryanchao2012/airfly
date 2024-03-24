from airfly.model import AirFly

from .entry import (
    create_entry_gcs,
    create_entry_group,
    delete_entry,
    delete_entry_group,
)
from .tag import (
    create_tag,
    create_tag_template,
    create_tag_template_field,
    delete_tag,
    delete_tag_template,
    delete_tag_template_field,
)


def _print_catalog():
    print("search_catalog")


# Search
class search_catalog(AirFly):
    operator_class = "PythonOperator"
    params = dict(python_callable=_print_catalog)

    upstream = (
        create_entry_gcs,
        create_entry_group,
        create_tag,
        create_tag_template,
        create_tag_template_field,
    )

    downstream = (
        delete_entry,
        delete_entry_group,
        delete_tag,
        delete_tag_template,
        delete_tag_template_field,
    )


class search_catalog_result(AirFly):
    operator_class = "BashOperator"
    params = dict(bash_command="echo search_catalog_result")

    upstream = search_catalog
