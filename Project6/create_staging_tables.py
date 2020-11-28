import configparser
import psycopg2
from staging_sql_queries import create_staging_table_queries, drop_staging_table_queries


def drop_staging_tables(cur, conn):
    """ Drop tables in Redshift if they exist """
    for query in drop_staging_table_queries:
        try:
            cur.execute(query)
            conn.commit()
        except Exception as e:
            print(e)


def create_staging_tables(cur, conn):
    """ Create tables in Redshift """
    for query in create_staging_table_queries:
        try:
            cur.execute(query)
            conn.commit()
        except Exception as e:
            print(e)


def main():
    """ Prepare ETL environment """
    config = configparser.ConfigParser()
    config.read('dwh.cfg')
    conn = psycopg2.connect("host={} dbname={} user={} password={} port={}".format(*config['CLUSTER'].values()))
    cur = conn.cursor()

    drop_staging_tables(cur, conn)
    create_staging_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()