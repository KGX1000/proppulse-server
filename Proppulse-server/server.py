from nba_api.stats.endpoints import playergamelog
from nba_api.stats.static import players
from flask import Flask, jsonify
from flask_cors import CORS
import os
import time

app = Flask(__name__)
CORS(app)

@app.route("/api/player/<int:player_id>")
def get_log_by_id(player_id):
    try:
        time.sleep(0.6)
        log = playergamelog.PlayerGameLog(
            player_id=player_id,
            season="2024-25"
        )
        data = log.get_dict()
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/player/name/<path:player_name>")
def get_log_by_name(player_name):
    try:
        matches = players.find_players_by_full_name(player_name)
        if not matches:
            return jsonify({"error": "Player not found", "name": player_name}), 404
        pid = matches[0]["id"]
        time.sleep(0.6)
        log = playergamelog.PlayerGameLog(
            player_id=pid,
            season="2024-25"
        )
        data = log.get_dict()
        data["resolved_id"] = pid
        data["resolved_name"] = matches[0]["full_name"]
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
