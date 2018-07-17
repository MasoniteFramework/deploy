""" A HerokuDBCommand Command """
from cleo import Command
import subprocess


class HerokuDBCommand(Command):
    """
    Description of command

    heroku:db
    """

    def handle(self):
        self.info('Setting Up Database ...')
        subprocess.call(['heroku', 'addons:create',
                         'heroku-postgresql:hobby-dev'])

        self.info('')
        self.info('Setting Up Environment Variables ...')

        database_url = bytes(subprocess.check_output(['heroku', 'config:get', 'DATABASE_URL'])).decode('utf-8')
        database_url = database_url.split(':')

        driver = database_url[0]
        user = database_url[1].replace('//', '')
        password = database_url[2].split('@')[0]
        host = database_url[2].split('@')[1]
        port = database_url[3].split('/')[0]
        database = database_url[3].split('/')[1].strip()

        subprocess.call(['heroku', 'config:set', 'DB_DRIVER={}'.format(driver)])
        subprocess.call(['heroku', 'config:set', 'DB_HOST={}'.format(host)])
        subprocess.call(['heroku', 'config:set', 'DB_USERNAME={}'.format(user)])
        subprocess.call(['heroku', 'config:set', 'DB_PASSWORD={}'.format(password)])
        subprocess.call(['heroku', 'config:set', 'DB_PORT={}'.format(port)])
        subprocess.call(['heroku', 'config:set', 'DB_DATABASE={}'.format(database)])
