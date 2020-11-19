from db.connect import connection

print('Imported module users.py')


def get_full_name(user):
    connection({'host': 'https://locahost:3000'})
    return '{0} {1}'.format(user['firstName'], user['lastName'])


def is_verified(user):
    if user.get('verified', False):
        print('Verified')
    else:
        print('Unverified')
    # try:
    #     if user['verified']:
    #         print('Boom Verified')
    # except KeyError:
    #     print('Unverfied, go away')
