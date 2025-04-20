from housing_tasks.preprocessing import preprocess_dataset
from housing_tasks.training import train_model

from airflow import DAG
from airflow.operators.python import PythonOperator

housing_dag = DAG(dag_id="housing_training", schedule_interval=None)

with housing_dag as dag:
    preprocess_task = PythonOperator(
        task_id="preprocess", python_callable=preprocess_dataset
    )

    train_task = PythonOperator(task_id="train_model", python_callable=train_model)

    preprocess_task >> train_task
