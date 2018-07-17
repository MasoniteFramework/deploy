''' A User Model Service Provider '''
from masonite.provider import ServiceProvider
from ..commands import HerokuDeployCommand
from ..commands import HerokuDBCommand
from ..commands import HerokuMigrateCommand
from ..commands import HerokuEnvCommand


class DeployProvider(ServiceProvider):
    ''' Binds the User model into the Service Container '''

    wsgi = False

    def register(self):
        ''' Registers The User Into The Service Container '''
        self.app.bind('HerokuDeployCommand', HerokuDeployCommand())
        self.app.bind('HerokuDBCommand', HerokuDBCommand())
        self.app.bind('HerokuMigrateCommand', HerokuMigrateCommand())
        self.app.bind('HerokuEnvCommand', HerokuEnvCommand())

    def boot(self):
        pass
