import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    def get_connection_string():
        # setup connection string
        # to do this, please define these environment variables first
        user_name = os.environ.get('PSQL_USER_NAME')
        password = os.environ.get('PSQL_PASSWORD')
        host = os.environ.get('PSQL_HOST')
        port = os.environ.get('PSQL_PORT')
        database_name = os.environ.get('PSQL_DB_NAME')

        env_variables_defined = user_name and password and host and database_name and port

        if env_variables_defined:
            # this string describes all info for psycopg2 to connect to the database
            return 'postgresql://{user_name}:{password}@{host}:{port}/{database_name}'.format(
                user_name=user_name,
                password=password,
                host=host,
                port=port,
                database_name=database_name
            )
        else:
            raise KeyError('Some necessary environment variable(s) are not defined')

    SQLALCHEMY_DATABASE_URI = (f"postgresql://ycodlzezvufkgu:ea03dc632820d4b31a79523fafbd99b2a0655a35dbf952fe28ac6932e7ed6ae7@ec2-63-32-248-14.eu-west-1.compute.amazonaws.com:5432/d2if87qkahch80")
    #SQLALCHEMY_DATABASE_URI = (get_connection_string(), "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    STATIC_FOLDER = f"{os.getenv('APP_FOLDER')}/project/static"
    MEDIA_FOLDER = f"{os.getenv('APP_FOLDER')}/project/media"