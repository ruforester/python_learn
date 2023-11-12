from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

station_list = pd.read_csv("weather-api/data-small/stations.txt", skiprows=17).to_html()

@app.route("/")
def home():
    return render_template("home.html", data=station_list)


@app.route("/api/v1/<station>/<date>")
def api(station, date):
    filename = f"weather-api/data-small/TG_STAID{str(station).zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature = df.loc[df['    DATE'] == date]['   TG'].squeeze()/10
    return {"station": station,
            "date": date,
            "temperature": temperature}

@app.route("/api/v1/<station>")
def station_all_dates(station):
    filename = f"weather-api/data-small/TG_STAID{str(station).zfill(6)}.txt"
    df = pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    result = df[['STAID', '    DATE', '   TG']].to_dict(orient='records')
    return result


if __name__ == "__main__":
    app.run(debug=True)
