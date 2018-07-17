""" A HerokuDeployCommand Command """
from cleo import Command


class HerokuDeployCommand(Command):
    """
    Deploy Your Application

    heroku:deploy
        {--a|app=None : The name of your Heroku Application}
    """

    def handle(self):
        import subprocess
        from config import application
        if self.option('app') == 'None':
            heroku_app = application.NAME.lower()
        else:
            heroku_app = self.option('app')

        output = subprocess.Popen(
            ['heroku', 'git:remote', '-a', heroku_app], stdout=subprocess.PIPE).communicate()[0]
        if not output:
            create_app = input(
                "App doesn't exist, would you like to craft one? [y/n]: ")  # Python 2
            if 'y' in create_app:
                subprocess.call(['heroku', 'create', heroku_app])
                subprocess.call(['heroku', 'git:remote', '-a', heroku_app])
                subprocess.call(['git', 'push', 'heroku', 'master'])
                key = subprocess.check_output(['craft', 'key'])
                key = bytes(key).decode('utf-8').replace('Key: ', '')
                self.info('')
                self.info('Storing Secet Key ...')
                subprocess.call(['heroku', 'config:set', 'KEY={}'.format(key)])
                subprocess.call(['craft', 'heroku:db'])
                subprocess.call(['craft', 'heroku:migrate'])
                subprocess.call(['heroku', 'open'])
        else:
            subprocess.call(['git', 'push', 'heroku', 'master'])
            subprocess.call(['craft', 'heroku:migrate'])
