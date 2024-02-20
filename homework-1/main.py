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


# load data from csv
def load_data_from_csv(conn: Any, file_path: str, table_name: str) -> None:
    with conn.cursor() as cur:
        with open(file_path) as file:
            next(file)

            rows = csv.reader(file)

            for row in rows:
                print(row)
                placeholders = ', '.join(['%s'] * len(row))
                query = f'INSERT INTO {table_name} VALUES ({placeholders})'
                cur.execute(query, row)
        conn.commit()
