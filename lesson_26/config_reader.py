import configparser

from lesson_26.constants import PATH_TO_PROJECT

abs_path = f'{PATH_TO_PROJECT}/config.ini'
config = configparser.RawConfigParser()
config.read(abs_path)


def get_connection():
    return config.get('mongo', 'connection_str')
