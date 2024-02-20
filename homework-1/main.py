"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2
from typing import Any


# connect to db
def connect_to_db() -> Any:
    conn = psycopg2.connect(
        database='north',
        host='localhost',
        password='2277',
        user='postgres')
    return conn


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


def main():
    conn = connect_to_db()

    try:
        load_data_from_csv(conn, 'north_data/customers_data.csv', 'customers')
        load_data_from_csv(conn, 'north_data/employees_data.csv', 'employees')
        load_data_from_csv(conn, 'north_data/orders_data.csv', 'orders')

        print('Данные успешно загружены в таблицы БД')
    except Exception as e:
        print(f'Возникла ошибка при загрузке данных: {e}')
    finally:
        conn.close()


if __name__ == '__main__':
    main()
