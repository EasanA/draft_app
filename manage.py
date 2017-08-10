import os
from flask_script import Manager
import xlrd

from draft import app
from draft.database import engine

manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

from draft.database import session, Player, Scoring
from draft.seed import seed, SeedParam
@manager.command
def seed_data():
    seedparam = SeedParam()
    seedparam.sheetname="playerprojectionvalueonly.xlsm"
    seedparam.namelow =3
    seedparam.namehigh =608
    seedparam.batterlow= 2
    seedparam.batterhigh= 351
    seedparam.pitcherlow =2
    seedparam.pitcherhigh =256 
    seed(seedparam)

from flask_migrate import Migrate, MigrateCommand
from draft.database import Base

class DB(object):
    def __init__(self, metadata):
        self.metadata = metadata

migrate = Migrate(app, DB(Base.metadata))
manager.add_command('db', MigrateCommand)

@manager.command
def clear():
    Base.metadata.drop_all(engine)

if __name__ == "__main__":
    manager.run()