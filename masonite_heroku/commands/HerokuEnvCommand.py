""" A HerokuEnv Command """
from cleo import Command
import subprocess


class HerokuEnvCommand(Command):
    """
    Manage Heroku Config Variables

    heroku:config
        {--g|get : Get the environment variables}
        {--s|set : Get the environment variables}
        {--e|env=production : Name of the environment file}

    """

    def handle(self):
        if self.option('get') :
            configs = bytes(subprocess.check_output(['heroku', 'config'])).decode('utf-8')
            configs = configs.split('\n')
            output = ""
            for key in configs:
                configs = [x for x in key.split(' ') if x]
                if len(configs) == 2 and key.split(':')[0] != 'DATABASE_URL':
                    output += "{}={}\n".format(key.split(':')[0], key.split(':')[1].strip())

            with open('.env.{}'.format(self.option('env')), 'w') as env_file:
                env_file.write(output)
            
            self.info('Added environment variables to .env.{}'.format(self.option('env')))

        elif self.option('set'):
            with open('.env.{}'.format(self.option('env'))) as env_file:
                content = env_file.readlines()

            for env in content:
                subprocess.call(['heroku', 'config:set', '{}={}'.format(env.split('=')[0], env.split('=')[1].replace('\n', ''))])