example dag forked from [here](https://github.com/apache/airflow/blob/main/airflow/example_dags/example_complex.py)

For this complex example, we can break down the tasks into several modules. It's quite similar to the case we deal with in practical situation. To build a big pipeline, we often need to design some abstract layers and manage the source codes into different logical scopes in order to keep the implementations maintainable and reusable as much as possible.

Imagine that if all codes were put into a single `DAG` context, after a few development iterations, it will probably become a disaster and hard to keep the structure anymore.

We can just simply generate the `dag.py` by `airfly`:
```
$ airfly --name example_complex --path .. --modname complex --dag-params params.py:dag_kwargs > dag.py
```
