from functools import lru_cache
from typing import Dict, Type

from airfly._dev.utils import collect_classes_and_functions, load_module_by_name
from airfly._vendor import airflow
from airfly.utils import qualname


@lru_cache()
def collect_airflow_operators() -> Dict[str, Type]:

    vendor = load_module_by_name(qualname(airflow))
    collected = {}
    for item in collect_classes_and_functions(vendor):
        if isinstance(item, type):

            basename = qualname(item, level=1)
            if basename not in collected:
                collected[basename] = []

            if item not in collected[basename]:
                collected[basename].append(item)

    return collected
