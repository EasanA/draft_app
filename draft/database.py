from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, ForeignKey

from . import app

engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

#League class, league specific scoring subclasses

class Player(Base):
    __tablename__ = 'players'
#create method to calculate cat scores/total scores 

    scoringindex = Column(Integer, ForeignKey('score.id'))
    
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    position = Column(String(128))
    batter_pa = Column(Integer)
    batter_ab = Column(Integer)
    batter_hit = Column(Integer)
    batter_single = Column(Integer)
    batter_double = Column(Integer)
    batter_triple = Column(Integer)
    batter_hr = Column(Integer)
    batter_bb = Column(Integer)
    batter_sb = Column(Integer)
    batter_cs = Column(Integer)
    batter_k = Column(Integer)
    batter_r = Column(Integer)
    batter_rbi = Column(Integer)
    batter_errors = Column(Integer)
    batter_gidp = Column(Integer)
    batter_hbp = Column(Integer)
    batter_xbh = Column(Integer)
    batter_avg = Column(Float)
    batter_obp = Column(Float)
    batter_slg = Column(Float)
    batter_ops = Column(Float)
    pitcher_w = Column(Float)
    pitcher_l = Column(Float)
    pitcher_ip = Column(Float)
    pitcher_hit = Column(Float)
    pitcher_bb = Column(Float)
    pitcher_k = Column(Float)
    pitcher_er = Column(Float)
    pitcher_s = Column(Float)
    pitcher_era = Column(Float)
    pitcher_whip = Column(Float)
    pitcher_k9 = Column(Float)
    pitcher_qs = Column(Float)
    pitcher_gs = Column(Float)
    pitcher_g = Column(Float)
    pitcher_hra = Column(Float)
    fantasy_points = 0
        
    def scoring(self, score):
        print('scoring method called')
        #score = session.query(Scoring).all()[0]
        if self.batter_single is not None and score.batter_single is not None:
            self.fantasy_points = self.batter_single * score.batter_single
            
class Scoring(Base):
    __tablename__ = 'score'

    players = relationship("Player", backref="scoring")
    
    id = Column(Integer, primary_key = True)
    batter_pa = Column(Integer)
    batter_ab = Column(Integer)
    batter_hit = Column(Integer)
    batter_single = Column(Integer)
    batter_double = Column(Integer)
    batter_triple = Column(Integer)
    batter_hr = Column(Integer)
    batter_bb = Column(Integer)
    batter_sb = Column(Integer)
    batter_cs = Column(Integer)
    batter_k = Column(Integer)
    batter_r = Column(Integer)
    batter_rbi = Column(Integer)
    batter_errors = Column(Integer)
    batter_gidp = Column(Integer)
    batter_hbp = Column(Integer)
    batter_xbh = Column(Integer)
    pitcher_w = Column(Float)
    pitcher_l = Column(Float)
    pitcher_ip = Column(Float)
    pitcher_hit = Column(Float)
    pitcher_bb = Column(Float)
    pitcher_k = Column(Float)
    pitcher_er = Column(Float)
    pitcher_s = Column(Float)
    pitcher_qs = Column(Float)
    pitcher_cg = Column(Float)
    pitcher_shutout = Column(Float)
    pitcher_hold = Column(Float)
    pitcher_gs = Column(Float)
    pitcher_hra = Column(Float)
    pitcher_bs = Column(Float)
    
   
Base.metadata.create_all(engine)