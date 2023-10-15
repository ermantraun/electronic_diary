
import psycopg2
from .data_checks import all_checks
from .sql_commands import sql_commands
def insert_in_database(data, data_type, db_config):
    with psycopg2.connect(dbname = db_config['dbname'], user = db_config['user'], 
                          password = db_config['password'], host = db_config['host'], port = db_config['port']) as conn:
        with conn.cursor() as curs:
            table = data_type
            curs.execute('SELECT * FROM "%s" WHERE  ', table)
            profile_exists = curs.fetchone()

            if profile_exists is None:
                pass
            else:
                result = 'CLIENT_ERROR: Profile already exists'
    return result


def add(data, data_type, db_config):

    data_is_not_correct = all_checks[data_type](data)
    if data_is_not_correct:
        return 'CLIENT_ERROR: ' + data_is_not_correct
    insert_result = insert_in_database(data, data_type, db_config)
    return insert_result
