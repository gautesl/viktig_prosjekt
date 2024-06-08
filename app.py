from flask import Flask
import Krabbeberegnemodul

app = Flask(__name__)



@app.route("/")
def home():
    antallKrabbeTonn = Krabbeberegnemodul.BeregnAntallKrabbeTonn()
    return f"Antall krabber som fiskes i norget ligger på rundt {antallKrabbeTonn} tonn i året"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)