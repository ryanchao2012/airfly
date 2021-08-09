# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.providers.google.cloud.operators.spanner import (
    SpannerDeleteDatabaseInstanceOperator,
    SpannerDeleteInstanceOperator,
    SpannerDeployDatabaseInstanceOperator,
    SpannerDeployInstanceOperator,
    SpannerQueryDatabaseInstanceOperator,
    SpannerUpdateDatabaseInstanceOperator,
)


class CloudSpannerInstanceDatabaseDeleteOperator(SpannerDeleteDatabaseInstanceOperator):
    pass


class CloudSpannerInstanceDatabaseDeployOperator(SpannerDeployDatabaseInstanceOperator):
    pass


class CloudSpannerInstanceDatabaseQueryOperator(SpannerQueryDatabaseInstanceOperator):
    pass


class CloudSpannerInstanceDatabaseUpdateOperator(SpannerUpdateDatabaseInstanceOperator):
    pass


class CloudSpannerInstanceDeleteOperator(SpannerDeleteInstanceOperator):
    pass


class CloudSpannerInstanceDeployOperator(SpannerDeployInstanceOperator):
    pass
