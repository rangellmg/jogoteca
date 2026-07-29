SECRET_KEY = 'alura'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{user}:{pwd}@{server}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        user='root',
        pwd='admin',
        server='localhost',
        database='jogoteca'
    )