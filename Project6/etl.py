import boto3
import configparser
import csv
import psycopg2
from sql_queries import insert_table_queries


def insert_tables(cur, conn):
    """ SQL queries insert data into fact and dimension tables """
    for query in insert_table_queries:
        try:
            cur.execute(query)
            conn.commit()
        except Exception as e:
            print(e)


def main():
    """ ETL pipeline for extracting from S3, transforming in Redshift and load into analysis tables """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')

    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(
        *config['CLUSTER'].values()))
    cur = conn.cursor()


    insert_tables(cur, conn)


    conn.close()


if __name__ == "__main__":
    main()

