#sample excel, feed data, test position
#sample excel, feed data, test formula

import os
import unittest

# Configure your app to use the testing database
os.environ["CONFIG_PATH"] = "draft.config.TestingConfig"

from draft import app
from draft.database import Base, engine, session, Scoring, Player
from draft.seed import seed,SeedParam

class TestViews(unittest.TestCase):
    def setUp(self):
        """ Test setup """
        self.client = app.test_client()

        # Set up the tables in the database
        Base.metadata.create_all(engine)

    def tearDown(self):
        """ Test teardown """
        session.close()
        # Remove the tables and their data from the database
        Base.metadata.drop_all(engine)
    
    def test_seed_data_position(self):
        seedparam = SeedParam()
        seedparam.sheetname="testdraftexcel.xlsm"
        seedparam.namelow =0
        seedparam.namehigh =3
        seedparam.batterlow= 1
        seedparam.batterhigh= 2
        seedparam.pitcherlow =1
        seedparam.pitcherhigh =3 
        seed(seedparam)
        players = session.query(Player).all()
        
        self.assertEqual(len(players), 3)
        print(players[0].name, players[0].position)
        self.assertEqual(players[0].position, "2B")
        print(players[1].name, players[1].position)
        self.assertEqual(players[1].position, "RP")
        print(players[2].name, players[2].position)
        self.assertEqual(players[2].position, "SP")
        
    
    def test_scoring(self):
        seedparam = SeedParam()
        seedparam.sheetname="testdraftexcel.xlsm"
        seedparam.namelow =0
        seedparam.namehigh =3
        seedparam.batterlow= 1
        seedparam.batterhigh= 2
        seedparam.pitcherlow =1
        seedparam.pitcherhigh =3 
        seed(seedparam)
        players = session.query(Player).all()
        score = session.query(Scoring).all()[0]
        for p in players:
            p.calculate_score(score)
        
        self.assertEqual(players[0].fantasy_points, 393.86)
        self.assertEqual(players[1].fantasy_points, 258.09)
        self.assertEqual(players[2].fantasy_points, 237.94)
if __name__ == "__main__":
    unittest.main()