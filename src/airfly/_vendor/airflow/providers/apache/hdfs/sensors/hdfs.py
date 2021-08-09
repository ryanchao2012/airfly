# Auto generated by 'inv collect-airflow'
from airfly._vendor.airflow.sensors.base import BaseSensorOperator


class HdfsSensor(BaseSensorOperator):
    filepath: "str"
    hdfs_conn_id: "str"
    ignored_ext: "typing.Union[typing.List[str], NoneType]"
    ignore_copying: "bool"
    file_size: "typing.Union[int, NoneType]"
    hook: "typing.Type[airflow.providers.apache.hdfs.hooks.hdfs.HDFSHook]"


class HdfsFolderSensor(HdfsSensor):
    be_empty: "bool"


class HdfsRegexSensor(HdfsSensor):
    regex: "typing.Pattern[str]"
