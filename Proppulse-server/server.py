from nba_api.stats.endpoints import playergamelog
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/player/<int:player_id>")
def get_log(player_id):
    log = playergamelog.PlayerGameLog(
        player_id=player_id,
        season="2024-25"
    )
    data = log.get_dict()
    return jsonify(data)

if __name__ == "__main__":
    app.run(port=5000)
