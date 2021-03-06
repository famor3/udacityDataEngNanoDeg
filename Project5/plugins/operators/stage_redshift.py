from airflow.contrib.hooks.aws_hook import AwsHook
from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults


class StageToRedshiftOperator(BaseOperator):
    ui_color = '#358140'
    template_fields = ("s3_key",)
    copy_sql = """
    COPY {}
    FROM '{}'
    ACCESS_KEY_ID '{}'
    SECRET_ACCESS_KEY '{}'
    FORMAT AS JSON 'auto'
    COMPUPDATE OFF REGION 'us-west-2'
    TIMEFORMAT AS 'epochmillisecs'
    """
    # TRUNCATECOLUMNS BLANKSASNULL EMPTYASNULL

    @apply_defaults
    def __init__(self,
                 redshift_conn_id='',
                 aws_credentials_id='',
                 table='',
                 s3_bucket='',
                 s3_key='',
                 *args, **kwargs):

        super(StageToRedshiftOperator, self).__init__(*args, **kwargs)
        self.table = table
        self.redshift_conn_id = redshift_conn_id
        self.s3_bucket = s3_bucket
        self.s3_key = s3_key
        self.aws_credentials_id = aws_credentials_id

    def execute(self, context):
        # Connect to AWS
        self.log.info('Connect to S3')
        aws_hook = AwsHook(self.aws_credentials_id)
        credentials = aws_hook.get_credentials()

        # Connect to Redshift
        self.log.info('Connect to Redshift')
        redshift = PostgresHook(postgres_conn_id=self.redshift_conn_id)

        # Clear current table from Redshift staging
        self.log.info(
            f'Remove records from staging table {self.table} in Redshift')
        redshift.run('DELETE FROM {}'.format(self.table))

        # Copy data from S3 to Redshift
        self.log.info(
            f'Copy and transfer data from S3 to Redshift staging table')

        rendered_key = self.s3_key.format(**context)
        s3_path = "s3://{}/{}".format(self.s3_bucket, rendered_key)
        formatted_sql = StageToRedshiftOperator.copy_sql.format(
            self.table,
            s3_path,
            credentials.access_key,
            credentials.secret_key
        )

        redshift.run(formatted_sql)
        self.log.info('Completed copy to staging table')
