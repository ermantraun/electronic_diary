import re
import psycopg2

def check_password(password):
    result = []
    if len(password) < 8:
        result.append('Password length is shorter than required')
    if not re.match(r'^[A-Za-z0-9]+$', password):
        result.append('The password contains not only letters of the Latin alphabet and numbers')

    if result:
        return '\n'.join(result)
    else:
        return ''

def check_email(email):
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        return 'Incorrect email'
    else:
        return ''


def check_initials(name, surname):
     
    initials = f'{name}:{surname}'
    if re.search(r'\s', initials):
        return 'The space character in the initials is not allowed'
    else:
        return ''

def check_data(data):
    password_is_correct = check_password(data['password'])
    email_is_correct = check_email(data['email'])
    initials_is_correct = check_initials(data['name'], data['surname'])

    if not any([password_is_correct, email_is_correct, initials_is_correct]):
        return ''
    else:
        return '\n'.join(log for log in (password_is_correct, email_is_correct, initials_is_correct) if log)
    
def insert_in_database(data, db_config):
    with psycopg2.connect(dbname = db_config['dbname'], user = db_config['user'], 
                          password = db_config['password'], host = db_config['host'], port = db_config['port']) as conn:
        with conn.cursor() as curs:
            table = 'classes'
            curs.execute('SELECT * FROM "%s" ', table)
            profile_exists = curs.fetchone()

            if profile_exists is None:
                pass
            else:
                result = 'CLIENT_ERROR: Profile already exists'
    return result
def add(data, db_config):

    data_is_not_correct = check_data(data)
    if data_is_not_correct:
        return 'CLIENT_ERROR: ' + data_is_not_correct
    insert_result = insert_in_database(data, db_config)
    return insert_result
