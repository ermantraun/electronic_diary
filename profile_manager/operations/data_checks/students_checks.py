import re

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
    