import requests
from flask import Flask, jsonify

url = 'https://gbfs.citibikenyc.com/gbfs/en/station_information.json'

app = Flask(__name__)

@app.route("/")
def index(): 
    return 0


@app.route("/api")
def api() :

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    
    else:
        
        return jsonify({
            "error8"

        }

        )
    return 0


if __name__ == "__main__":
    app.run()
