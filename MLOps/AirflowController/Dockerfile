# syntax=docker/dockerfile:1
FROM apache/airflow:2.2.2-python3.8

COPY requirements.txt /util/requirements.txt
COPY requirements-test.txt /util/requirements-test.txt
RUN pip install --no-cache-dir -r /util/requirements.txt

COPY data /opt/airflow/dags
