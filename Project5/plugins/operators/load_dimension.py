from airflow.hooks.postgres_hook import PostgresHook
from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults

class LoadDimensionOperator(BaseOperator):

    ui_color = '#80BD9E'

    @apply_defaults
    def __init__(self,
                 redshift_conn_id='',
                 table='',
                 sql='',
                 mode='delete_load',
                 *args, **kwargs):

        super(LoadDimensionOperator, self).__init__(*args, **kwargs)
        self.redshift_conn_id=redshift_conn_id
        self.table=table
        self.sql=sql
        self.mode=mode

    def execute(self, context):
        redshift=PostgresHook(postgres_conn_id=self.redshift_conn_id)
        
        if self.mode=='delete_load':
            # Clear data from DIM TABLE
            self.log.info('Refreshing data in table %s' % self.table)
            clear_statement = 'DELETE FROM %s' % self.table
            redshift.run(clear_statement)
            
            # Write data to DIM TABLE
            self.log.info('Starting to load dim table %s' % self.table)
            sql='INSERT INTO %s %s' % (self.table, self.sql)
            redshift.run(sql)
            self.log.info('Dim table %s load finished' % self.table)
            
        elif self.mode=='append':
            # Append or add new data to DIM TABLE
            self.log.info('Starting to load dim table %s' % self.table)
            sql='INSERT INTO %s %s' % (self.table, self.sql)
            redshift.run(sql)
            self.log.info('Dim table %s load finished' % self.table)
            
        else:
            msg='Invalid mode. Mode must be one of "append" or "delete_load"'
            self.log.error(msg)
            
            

