example dag forked from [here](https://github.com/apache/airflow/blob/main/airflow/example_dags/example_bash_operator.py)


Generate `dag.py` by `airfly`
```
$ airfly --name example_bash_operator --modname workflow --dag-params params.py:dag_kwargs > dag.py
```