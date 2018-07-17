""" A HerokuMigrate Command """
from cleo import Command
import subprocess


class HerokuMigrateCommand(Command):
    """
    Description of command

    heroku:migrate
    """

    def handle(self):
        self.info('')
        self.info('Running Migrations ...')
        subprocess.call(['heroku', 'run', 'craft', 'migrate'])