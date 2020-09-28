from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class DataQualityOperator(BaseOperator):

    ui_color = '#89DA59'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id='',
                 tables=[],
                 chk_sql='SELECT COUNT(*) FROM %s',
                 *args, **kwargs):

        super(DataQualityOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id=redshift_conn_id
        self.tables=tables
        self.chk_sql=chk_sql

    def execute(self, context):
        redshift=PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        for table in self.tables:
            recs=redshift.get_records(
                self.chk_sql.format(table)
            )
            if (len(recs) < 1) or (len(recs[0]) < 0):
                self.log.error("Table %s is empty".format(table))
                raise ValueError(
                    "Table %s failed data quality operator".format(table)
                )
                num_records = recs[0][0]
            if num_records == 0:
                self.log.error("No records found in {}".format(table))
                raise ValueError("No records found in {}".format(table))
                pass_msg="Data Quality check passed on table {}".format(table)
                self.log.info(pass_msg)
