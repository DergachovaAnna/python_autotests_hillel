import configparser

from lesson_19.constants import PATH_TO_PROJECT

abs_path = f'{PATH_TO_PROJECT}/configurations/configuration.ini'
config = configparser.RawConfigParser()
config.read(abs_path)


def get_site_url():
    return (config.get('site_data', 'site_url_en'),
            config.get('site_data', 'site_url_pl'))


def get_user_creds():
    return (config.get('user_data', 'email'),
            config.get('user_data', 'password'))


def get_browser_id():
    return config.get('browser_data', 'browser_id')
