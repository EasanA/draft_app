from flask import render_template

from . import app
from .database import session, Player, Scoring

@app.route("/")
def player():
    players = session.query(Player).all()
    score = session.query(Scoring).all()[0]
    for p in players:
        p.calculate_score(score)
    sorted_players = sorted(players, key = lambda player: player.fantasy_points, reverse=True)     
    return render_template("players.html",
        players=sorted_players
    )