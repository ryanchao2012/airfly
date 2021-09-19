# airfly: Auto generate airflow's `dag.py` on the fly

Data pipeline management is essential for data engineering in company, many data teams rely on tools like Airflow to help them organize the task workflows, such as ETL, data analytic jobs or even the machine learning projects.

Airflow provides an interface to let developers arrange workloads into a sequence of "operators", and declare the task dependencies while writing the `dag.py` file. 

For some development or management reasons, one may use separate `DAGs` to build workflows for different data projects, but doing so also isolates the potential dependencies between pipelines while they may often share common resources, such as the same data sources or processing logics, leading to repeated implementations or have to take additional efforts(e.g., `Sensors`) for linking the tasks between different DAGs.

Instead, if we organize all tasks within a centralized-DAG, although it keeps the code as much reusable as possible, as the workflow grows, the dependencies 

<!-- As the scalability grows, things are getting challenging -->


# Usage

## Define `AirflowTask` with Airflow operator

```

```


## Declare task dependency


## Generate the `dag.py` file
```
$ airfly --name my_dag --modname tasks > dag.py
```

## Assign `DAG` parameters


## Exclude tasks from dependency tree
