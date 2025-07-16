from dagster import job, op, get_dagster_logger

@op
def say_hello():
    logger = get_dagster_logger()
    logger.info("👋 Hello from Dagster!")

@job
def hello_dag():
    say_hello()
