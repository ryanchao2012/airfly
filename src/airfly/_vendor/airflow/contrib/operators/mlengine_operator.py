# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.google.cloud.operators.mlengine import (
    MLEngineManageModelOperator,
    MLEngineManageVersionOperator,
    MLEngineStartBatchPredictionJobOperator,
    MLEngineStartTrainingJobOperator,
)


class MLEngineBatchPredictionOperator(MLEngineStartBatchPredictionJobOperator):
    pass


class MLEngineModelOperator(MLEngineManageModelOperator):
    pass


class MLEngineTrainingOperator(MLEngineStartTrainingJobOperator):
    pass


class MLEngineVersionOperator(MLEngineManageVersionOperator):
    pass
