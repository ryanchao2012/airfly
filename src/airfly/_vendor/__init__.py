from functools import lru_cache
from typing import Dict, Type

from airfly._vendor import airflow
from airfly.utils import collect_objects, load_module_by_name, qualname


@lru_cache()
def collect_airflow_operators() -> Dict[str, Type]:

    vendor = load_module_by_name(qualname(airflow))
    collected = {}

    for item in collect_objects(vendor, lambda obj: isinstance(obj, type)):

        basename = qualname(item, level=1)
        if basename not in collected:
            collected[basename] = []

        if item not in collected[basename]:
            collected[basename].append(item)

    return collected
