from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import MigrateCommand, Migrate
from app.models import Blog, User, Review, Role


# app = create_app('development')

app = create_app('production')


manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def test():

    import unittest

    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():

    return dict(app=app, db=db, Blog=Blog, User=User, Review=Review, Role=Role)


if __name__ == '__main__':
    manager.run()