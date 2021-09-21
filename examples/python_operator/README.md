example dag forked from [here](https://github.com/apache/airflow/blob/main/airflow/example_dags/example_python_operator.py)


Generate `dag.py` by `airfly`
```
$ airfly --name example_python_operator --modname workflow --dag-params params.py:dag_kwargs > dag.py
```