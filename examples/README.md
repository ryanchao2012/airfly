
**Generate `DAG` for entire `examples` module**

```
$ airfly --name examples --path .. --modname examples -d params.py:dag_kwargs > dag.py
```

**Graph View in Airflow WebUI**

![](../assets/view.png)