from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import sys
from pathlib import Path

#Ajouter le chemin du répertoire parent à sys.path
sys.path.append(str(Path(__file__).resolve().parents[1]))

#Importer la fonction de tâche depuis le fichier correspondant
from tasks.task_extract import task_extract

def task2():
    tableau = [1, 2, 3, 4, 5]
    print("Données stockées dans le tableau :", tableau)

def task3():
    print("Good Bye World")
    # Utilisez ici le tableau créé dans la tâche précédente

def task4():
    print("Helloooooo")

with DAG( 

    dag_id='Dataflow_usecase',
    start_date=datetime(2023, 6, 13),
    description='affichage dans la console et création de tableau',
    schedule_interval="@daily",
    catchup = False
) as dag :

    task_1 = PythonOperator(
        task_id='task_extract',
        python_callable=task_extract,
        dag=dag
    )

    task_2 = PythonOperator(
        task_id='task_2',
        python_callable=task2,
        dag=dag
    )

    task_3 = PythonOperator(
        task_id='task_3',
        python_callable=task3,
        dag=dag
    )

    task_4 = PythonOperator(
        task_id='task_4',
        python_callable=task4,
        dag=dag
    )

task_1 >> task_2 >> task_3 >> task_4