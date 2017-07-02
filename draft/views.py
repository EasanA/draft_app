from flask import render_template

from . import app
from .database import session, Player, Scoring

@app.route("/")
def player():
    players = session.query(Player).all()
    score = session.query(Scoring).all()[0]
    #print(score)
    for p in players:
        if p.batter_single is not None and score.batter_single is not None:
        #p.scoring(score)
        #print(p.batter_single)
        #print(score.batter_single)
            p.fantasy_points = round((p.batter_single * score.batter_single + 
            p.batter_double * score.batter_double + p.batter_triple * 
            score.batter_triple + p.batter_hr * score.batter_hr + p.batter_bb *
            score.batter_bb + p.batter_sb * score.batter_sb + p.batter_cs *
            score.batter_cs + p.batter_k * score.batter_k + p.batter_r * 
            score.batter_r + p.batter_rbi * score.batter_rbi),1)
            
        else:
            p.fantasy_points = round((p.pitcher_w * score.pitcher_w + 
            p.pitcher_l * score.pitcher_l + p.pitcher_ip *score.pitcher_ip + 
            p.pitcher_hit * score.pitcher_hit + p.pitcher_bb * score.pitcher_bb 
            + p.pitcher_k * score.pitcher_k + p.pitcher_er * score.pitcher_er + 
            p.pitcher_s * score.pitcher_s + p.pitcher_qs * score.pitcher_qs),0)
    sorted_players = sorted(players, key = lambda player: player.fantasy_points, reverse=True)     
    return render_template("players.html",
        players=sorted_players
    )