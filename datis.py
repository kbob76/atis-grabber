import requests
import pprint
import json
import flask

app = flask.Flask(__name__)

def get_atis_data(airport_code):
    print(f"Incoming request for airport code {airport_code}")
    try:
        atis_data_api = f"https://datis.clowd.io/api/{airport_code}"
        response = requests.get(atis_data_api)
        atis_data = response.json()
        print(atis_data)
        if atis_data:
            return atis_data[0]
        else:
            print("Unable to retrieve ATIS data")
            return None
    except requests.exceptions.RequestException:
        print(f"Error fetching data from API {e}")
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    """Basic index page that you land on"""
    
    atis_data = None
    airport_icao = None
    if flask.request.method == 'POST':
        airport_icao = flask.request.form.get('icao')
        print(f"Entered airport code: {airport_icao}")
        if airport_icao:
            atis_data = get_atis_data(airport_icao.upper())
    
    return flask.render_template('index.html', atis_data=atis_data, airport_icao=airport_icao)
    
if __name__ == "__main__":
    app.run(debug=True)