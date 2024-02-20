"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2
from typing import Any


# connect to db
def connect_to_db() -> Any:
    return psycopg2.connect(
        database='north',
        host='localhost',
        password='2277',
        user='postgres')



