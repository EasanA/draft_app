from flask import render_template

from . import app
from .database import session, Player, Scoring

@app.route("/points")
def points():
    players = session.query(Player).all()
    score = session.query(Scoring).all()[0]
    for p in players:
        p.calculate_score(score)
    sorted_players = sorted(players, key = lambda player: player.fantasy_points, reverse=True)     
    return render_template("points.html",
        players=sorted_players
    )
    
@app.route("/setting")
def scoring():
    score = session.query(Scoring).all()[0]
    return render_template("scoringsetting.html",
    score = score
    )
    
from flask import request, redirect, url_for
    
@app.route("/setting", methods=["POST"])
def add_socring():
    score = session.query(Scoring).all()[0]
    if score is None:
        score = Scoring(
            batter_pa=request.form["batter_pa"],
            batter_ab=request.form["batter_ab"],
            batter_hit=request.form["batter_hit"],
            batter_single=request.form["batter_single"],
            batter_double=request.form["batter_double"],
            batter_triple=request.form["batter_triple"],
            batter_hr=request.form["batter_hr"],
            batter_bb=request.form["batter_bb"],
            batter_sb=request.form["batter_sb"],
            batter_cs=request.form["batter_cs"],
            batter_k=request.form["batter_k"],
            batter_r=request.form["batter_r"],
            batter_rbi=request.form["batter_rbi"],
            batter_errors=request.form["batter_errors"],
            batter_gidp=request.form["batter_gidp"],
            batter_hbp=request.form["batter_hbp"],
            batter_xbh=request.form["batter_xbh"],
            pitcher_w=request.form["pitcher_w"],
            pitcher_l=request.form["pitcher_l"],
            pitcher_ip=request.form["pitcher_ip"],
            pitcher_hit=request.form["pitcher_hit"],
            pitcher_bb=request.form["pitcher_bb"],
            pitcher_k=request.form["pitcher_k"],
            pitcher_er=request.form["pitcher_er"],
            pitcher_s=request.form["pitcher_s"],
            pitcher_qs=request.form["pitcher_qs"],
            pitcher_cg=request.form["pitcher_cg"],
            pitcher_shutout=request.form["pitcher_shutout"],
            pitcher_hold=request.form["pitcher_hold"],
            pitcher_gs=request.form["pitcher_gs"],
            pitcher_hra=request.form["pitcher_hra"],
            pitcher_bs=request.form["pitcher_bs"],
        )
    else:
        score.batter_pa=request.form["batter_pa"],
        score.batter_ab=request.form["batter_ab"],
        score.batter_hit=request.form["batter_hit"],
        score.batter_single=request.form["batter_single"],
        score.batter_double=request.form["batter_double"],
        score.batter_triple=request.form["batter_triple"],
        score.batter_hr=request.form["batter_hr"],
        score.batter_bb=request.form["batter_bb"],
        score.batter_sb=request.form["batter_sb"],
        score.batter_cs=request.form["batter_cs"],
        score.batter_k=request.form["batter_k"],
        score.batter_r=request.form["batter_r"],
        score.batter_rbi=request.form["batter_rbi"],
        score.batter_errors=request.form["batter_errors"],
        score.batter_gidp=request.form["batter_gidp"],
        score.batter_hbp=request.form["batter_hbp"],
        score.batter_xbh=request.form["batter_xbh"],
        score.pitcher_w=request.form["pitcher_w"],
        score.pitcher_l=request.form["pitcher_l"],
        score.pitcher_ip=request.form["pitcher_ip"],
        score.pitcher_hit=request.form["pitcher_hit"],
        score.pitcher_bb=request.form["pitcher_bb"],
        score.pitcher_k=request.form["pitcher_k"],
        score.pitcher_er=request.form["pitcher_er"],
        score.pitcher_s=request.form["pitcher_s"],
        score.pitcher_qs=request.form["pitcher_qs"],
        score.pitcher_cg=request.form["pitcher_cg"],
        score.pitcher_shutout=request.form["pitcher_shutout"],
        score.pitcher_hold=request.form["pitcher_hold"],
        score.pitcher_gs=request.form["pitcher_gs"],
        score.pitcher_hra=request.form["pitcher_hra"],
        score.pitcher_bs=request.form["pitcher_bs"],
    session.add(score)
    session.commit()
    return redirect(url_for('player'))
    
@app.route("/glossary")
def glossary():
    return render_template("glossary.html"
    )
    
@app.route("/")
def homepage():
    return render_template("homepage.html"
    )
    
@app.route("/position/<position>")
def positional(position):
    if position in ['SP', 'RP', 'C', '1B','2B','3B','SS', 'OF','DH']:
        players = session.query(Player).filter_by(position=position).all()
        score = session.query(Scoring).all()[0]
        for p in players:
            p.calculate_score(score)
        sorted_players = sorted(players, key = lambda player: player.fantasy_points, reverse=True)
    elif position == 'CI':
        players = session.query(Player).filter(Player.position.in_ (['1B','3B'])).all()
        score = session.query(Scoring).all()[0]
        for p in players:
            p.calculate_score(score)
        sorted_players = sorted(players, key = lambda player: player.fantasy_points, reverse=True)
    elif position == 'MI':
        players = session.query(Player).filter(Player.position.in_ (['2B','SS'])).all()
        score = session.query(Scoring).all()[0]
        for p in players:
            p.calculate_score(score)
        sorted_players = sorted(players, key = lambda player: player.fantasy_points, reverse=True)
    elif position == 'IF':
        players = session.query(Player).filter(Player.position.in_ (['1B','2B','3B','SS'])).all()
        score = session.query(Scoring).all()[0]
        for p in players:
            p.calculate_score(score)
        sorted_players = sorted(players, key = lambda player: player.fantasy_points, reverse=True)
    elif position == 'U':
        players = session.query(Player).filter(Player.position.in_ (['C', '1B','2B','3B','SS', 'OF','DH'])).all()
        score = session.query(Scoring).all()[0]
        for p in players:
            p.calculate_score(score)
        sorted_players = sorted(players, key = lambda player: player.fantasy_points, reverse=True)
    elif position == 'P':
        players = session.query(Player).filter(Player.position.in_ (['SP', 'RP'])).all()
        score = session.query(Scoring).all()[0]
        for p in players:
            p.calculate_score(score)
        sorted_players = sorted(players, key = lambda player: player.fantasy_points, reverse=True)
    else:
        players = session.query(Player).all()
        score = session.query(Scoring).all()[0]
        for p in players:
            p.calculate_score(score)
        sorted_players = sorted(players, key = lambda player: player.fantasy_points, reverse=True)
    return render_template("position.html",
        players=sorted_players
    )
    
@app.route("/playerpage/<id>")
def playerpage(id):
    player = session.query(Player).get(id)
    score = session.query(Scoring).all()[0]
    player.calculate_score(score)
    player.calculate_per_pa()
    player.calculate_per_ip()
    return render_template("playerpage.html",
        player=player
    )
    
@app.route("/", methods=['POST'])
def search(string):
    string =request.form["search"]
    return redirect(url_for('playersearch', string = string))

from sqlalchemy import func

@app.route("/search", methods=['POST'])
def playerlist():
    search_string =request.form["search"]
    print(search_string)
    players = session.query(Player).filter(func.lower(Player.name).contains(func.lower(search_string))).all()
    score = session.query(Scoring).all()[0]
    for p in players:
        p.calculate_score(score)
    sorted_players = sorted(players, key = lambda player: player.fantasy_points, reverse=True)     
    return render_template("playersearch.html",
        players=sorted_players
    )
