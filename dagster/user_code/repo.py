from dagster import Definitions
from .jobs.hello_job import hello_dag

definitions = Definitions(
    jobs=[hello_dag]
)
