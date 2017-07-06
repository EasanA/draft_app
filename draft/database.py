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
    batter_pa = Column(Integer, default = 0)
    batter_ab = Column(Integer, default = 0)
    batter_hit = Column(Integer, default = 0)
    batter_single = Column(Integer, default = 0)
    batter_double = Column(Integer, default = 0)
    batter_triple = Column(Integer, default = 0)
    batter_hr = Column(Integer, default = 0)
    batter_bb = Column(Integer, default = 0)
    batter_sb = Column(Integer, default = 0)
    batter_cs = Column(Integer, default = 0)
    batter_k = Column(Integer, default = 0)
    batter_r = Column(Integer, default = 0)
    batter_rbi = Column(Integer, default = 0)
    batter_errors_per_pa = Column(Float, default = 0)
    batter_gidp_per_pa = Column(Float, default = 0)
    batter_hbp_per_pa = Column(Float, default = 0)
    batter_xbh = Column(Integer, default = 0)
    batter_avg = Column(Float, default = 0)
    batter_obp = Column(Float, default = 0)
    batter_slg = Column(Float, default = 0)
    batter_ops = Column(Float, default = 0)
    pitcher_w = Column(Float, default = 0)
    pitcher_l = Column(Float, default = 0)
    pitcher_ip = Column(Float, default = 0)
    pitcher_hit = Column(Float, default = 0)
    pitcher_bb = Column(Float, default = 0)
    pitcher_k = Column(Float, default = 0)
    pitcher_er = Column(Float, default = 0)
    pitcher_s = Column(Float, default = 0)
    pitcher_era = Column(Float, default = 0)
    pitcher_whip = Column(Float, default = 0)
    pitcher_k9 = Column(Float, default = 0)
    pitcher_qs = Column(Float, default = 0)
    pitcher_gs = Column(Float, default = 0)
    pitcher_g = Column(Float, default = 0)
    pitcher_hra = Column(Float, default = 0)
    pitcher_cg_per_gs = Column(Float, default = 0)
    pitcher_shutout_per_gs = Column(Float, default = 0)
    pitcher_hold = Column(Float, default = 0)
    pitcher_bs = Column(Float, default = 0)
    fantasy_points = 0
        
    def calculate_score(self, score):
            self.fantasy_points = round((self.batter_pa * score.batter_pa + 
            self.batter_ab * score.batter_ab + self.batter_hit * 
            score.batter_hit + self.batter_single * score.batter_single + 
            self.batter_double * score.batter_double + self.batter_triple * 
            score.batter_triple + self.batter_hr * score.batter_hr +
            self.batter_bb * score.batter_bb + self.batter_sb * score.batter_sb 
            + self.batter_cs * score.batter_cs + self.batter_k * score.batter_k 
            + self.batter_r * score.batter_r + self.batter_rbi * 
            score.batter_rbi + self.batter_errors_per_pa * self.batter_pa * 
            score.batter_errors + self.batter_gidp_per_pa * self.batter_pa * 
            score.batter_gidp + self.batter_hbp_per_pa *self.batter_pa * 
            score.batter_hbp + self.batter_xbh * score.batter_xbh + 
            self.pitcher_w * score.pitcher_w + self.pitcher_l * score.pitcher_l 
            + self.pitcher_ip *score.pitcher_ip + self.pitcher_hit * 
            score.pitcher_hit + self.pitcher_bb * score.pitcher_bb + 
            self.pitcher_k * score.pitcher_k + self.pitcher_er * 
            score.pitcher_er + self.pitcher_s * score.pitcher_s + 
            self.pitcher_qs * score.pitcher_qs + self.pitcher_gs * 
            score.pitcher_gs + self.pitcher_hra * score.pitcher_hra + 
            self.pitcher_cg_per_gs * self.pitcher_gs * score.pitcher_cg + 
            self.pitcher_shutout_per_gs * self.pitcher_gs * 
            score.pitcher_shutout + self.pitcher_hold * score.pitcher_hold + 
            self.pitcher_bs * score.pitcher_bs ),1)
            
class Scoring(Base):
    __tablename__ = 'score'

    players = relationship("Player", backref="scoring")
    
    id = Column(Integer, primary_key = True)
    batter_pa = Column(Integer, default = 0)
    batter_ab = Column(Integer, default = 0)
    batter_hit = Column(Integer, default = 0)
    batter_single = Column(Integer, default = 0)
    batter_double = Column(Integer, default = 0)
    batter_triple = Column(Integer, default = 0)
    batter_hr = Column(Integer, default = 0)
    batter_bb = Column(Integer, default = 0)
    batter_sb = Column(Integer, default = 0)
    batter_cs = Column(Integer, default = 0)
    batter_k = Column(Integer, default = 0)
    batter_r = Column(Integer, default = 0)
    batter_rbi = Column(Integer, default = 0)
    batter_errors = Column(Integer, default = 0)
    batter_gidp = Column(Integer, default = 0)
    batter_hbp = Column(Integer, default = 0)
    batter_xbh = Column(Integer, default = 0)
    pitcher_w = Column(Float, default = 0)
    pitcher_l = Column(Float, default = 0)
    pitcher_ip = Column(Float, default = 0)
    pitcher_hit = Column(Float, default = 0)
    pitcher_bb = Column(Float, default = 0)
    pitcher_k = Column(Float, default = 0)
    pitcher_er = Column(Float, default = 0)
    pitcher_s = Column(Float, default = 0)
    pitcher_qs = Column(Float, default = 0)
    pitcher_cg = Column(Float, default = 0)
    pitcher_shutout = Column(Float, default = 0)
    pitcher_hold = Column(Float, default = 0)
    pitcher_gs = Column(Float, default = 0)
    pitcher_hra = Column(Float, default = 0)
    pitcher_bs = Column(Float, default = 0)
    
   
Base.metadata.create_all(engine)