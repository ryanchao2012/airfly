import importlib
from functools import lru_cache
from typing import Dict, Type

from airfly._vendor import airflow
from airfly.utils import collect_objects, qualname


@lru_cache()
def collect_airflow_operators() -> Dict[str, Type]:

    vendor = importlib.import_module(qualname(airflow))
    collected = {}

    for item in collect_objects(vendor, lambda obj: isinstance(obj, type)):

        basename = qualname(item, level=1)
        if basename not in collected:
            collected[basename] = []

        if item not in collected[basename]:
            collected[basename].append(item)

    return collected
