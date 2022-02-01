import flask
from flask import request, jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = True
# Define list of countries that have/need to visit
trips = [
    {
        "id": 1,
        "country": "Spain",
        "visited": "yes",
        "airport": "Barcelona"
    },
    {
        "id": 2,
        "country": "UK",
        "visited": "no",
        "airport": "London"
    },
    {
        "id": 3,
        "country": "Portugal",
        "visited": "no",
        "airport": "Lisbon"
    },
    {
        "id": 4,
        "country": "Australia",
        "visited": "no",
        "airport": "Melbourne"
    },
    {
        "id": 5,
        "country": "Germany",
        "visited": "no",
        "airport": "Berlin"
    },
    {
        "id": 6,
        "country": "Italy",
        "visited": "no",
        "airport": "Rome"
    },
    {
        "id": 7,
        "country": "Sweden",
        "visited": "no",
        "airport": "Stockholm"
    }
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1 style="text-align:center;">Trip Tracker App</h1>
                <p style="text-align:center;color:tomato;font-size:160%">Flask app that tracks trip information.</p>'''


@app.route('/api/v1/trips/all', methods=['GET'])
def api_all():
    return jsonify(trips)


@app.route('/api/v1/trips', methods=['GET'])
def api_id():
    results = []
    if 'id' in request.args:
        id = int(request.args['id'])
        for trip in trips:
            if trip['id'] == id:
                results.append(trip)
        return jsonify(results)
    else:
        return "Error: No id field provided. Please specify a trip 'id', 'country', 'visited', 'airport' values."


@app.route("/api/v1/trips",  methods=['POST'])
def api_insert():
    trip = request.get_json(silent=True)

    if 'id' in request.get_json():
        trips.append(trip)
        return "Success: Trip information has been added."
    else:
        return "You must provide a json value with keys: id:[int], country:[str], visited:[str], airport:[str]."


@app.route("/api/v1/trips/<id>", methods=["DELETE"])
def api_delete(id):
    for trip in trips:
        if trip['id'] == int(id):
            trips.remove(trip)
            return "Success: Trip information has been deleted."
    return "You must specify a valid 'id' to delete."


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

