import os
from flask_script import Manager
import xlrd

from draft import app

manager = Manager(app)

@manager.command
def run():
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

from draft.database import session, Player, Scoring    
@manager.command
def seed():
    book = xlrd.open_workbook("2017PointsDraftCheatsheetv2.55.xlsm")
    sheet1 = book.sheet_by_name("Projection-H")
    
    for j in range(2,32):
        batter= Player(
            name = sheet1.cell(j,0).value,
            batter_pa = sheet1.cell(j,2).value,
            batter_ab = sheet1.cell(j,3).value,
            batter_r = sheet1.cell(j,4).value,
            batter_hit = sheet1.cell(j,5).value,
            batter_single =sheet1.cell(j,6).value,
            batter_double = sheet1.cell(j,7).value,
            batter_triple = sheet1.cell(j,8).value,
            batter_hr = sheet1.cell(j,9).value,
            batter_bb = sheet1.cell(j,13).value,
            batter_sb = sheet1.cell(j,11).value,
            batter_cs = sheet1.cell(j,12).value,
            batter_k =sheet1.cell(j,14).value,
            batter_rbi = sheet1.cell(j,10).value,
            batter_avg = round(sheet1.cell(j,15).value,4),
            batter_obp = round(sheet1.cell(j,16).value,4),
            batter_slg = round(sheet1.cell(j,17).value,4),
            batter_ops = round(sheet1.cell(j,18).value,4),
        )
        session.add(batter)
        session.commit()
    
    sheet2 = book.sheet_by_name("Projection-P")
    
    for j in range(2,32):
        pitcher = Player(
            name = sheet2.cell(j,0).value,
            pitcher_w = round(sheet2.cell(j,2).value,4),
            pitcher_l = round(sheet2.cell(j,3).value,4),
            pitcher_ip = round(sheet2.cell(j,4).value,4),
            pitcher_hit = round(sheet2.cell(j,5).value,4),
            pitcher_bb = round(sheet2.cell(j,6).value,4),
            pitcher_k = round(sheet2.cell(j,7).value,4),
            pitcher_er = round(sheet2.cell(j,8).value,4),
            pitcher_s = round(sheet2.cell(j,9).value,2),
            pitcher_era = round(sheet2.cell(j,10).value,4),
            pitcher_whip = round(sheet2.cell(j,11).value,4),
            pitcher_k9 = round(sheet2.cell(j,12).value,4),
            pitcher_qs =sheet2.cell(j,13).value,
            pitcher_gs = round(sheet2.cell(j,14).value,4),
            pitcher_g = round(sheet2.cell(j,15).value,4),
            pitcher_hra = round(sheet2.cell(j,16).value,4),
        )
        session.add(pitcher)
        session.commit()
    
    score = Scoring(
            batter_single = 1,
            batter_double = 2,
            batter_triple = 3,
            batter_hr = 4,
            batter_bb = 1,
            batter_sb = 2,
            batter_cs = -1,
            batter_k = -1,
            batter_r = 1,
            batter_rbi = 1,
            pitcher_w = 5,
            pitcher_l = -5,
            pitcher_ip = 1.5,
            pitcher_hit = -.5,
            pitcher_bb = -1,
            pitcher_k = 1,
            pitcher_er = -1,
            pitcher_s = 10,
            pitcher_qs = 10,
            pitcher_shutout = 10,
            pitcher_bs = -5,
        )
    session.add(score)
    session.commit()
    
from flask_migrate import Migrate, MigrateCommand
from draft.database import Base

class DB(object):
    def __init__(self, metadata):
        self.metadata = metadata

migrate = Migrate(app, DB(Base.metadata))
manager.add_command('db', MigrateCommand)

@manager.command
def clear():
    batters_deleted = session.query(Player).delete()
    scoring_deleted = session.query(Scoring).delete()
    session.commit()

if __name__ == "__main__":
    manager.run()