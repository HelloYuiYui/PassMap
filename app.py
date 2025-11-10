import pandas as pd
import numpy as np
from flask import Flask, render_template
from os.path import join, dirname, realpath
import numpy as np

app = Flask(__name__, template_folder="")

def clean(df):
    objd = {
        'no admission':  list(df["Destination_ISO2"][(df.Mobility == 0)].values),
        'visarequired':  list(df["Destination_ISO2"][(df.Mobility == 1)].values),
        'visaonarrival': list(df["Destination_ISO2"][df.Requirement == "visa on arrival"].values),
        'visaeta':       list(df["Destination_ISO2"][df.Requirement.isin(["e-visa", "eta"])].values),
        'visafree':      list(df["Destination_ISO2"][(df.Mobility >= 3)][(df.Mobility < 4)].values),
        'FoM':           list(df["Destination_ISO2"][df.Requirement == "FoM"].values),
        'self':          list(df["Destination_ISO2"][df.Requirement == "-1"].values)
    }

    return objd

@app.route("/")
def index():
    return render_template("./map.html")

@app.route("/country/<passport>", methods=['GET'])
def getCountries(passport):
    try:
        df = pd.read_csv(join(dirname(realpath(__file__)), 'static/passport-index-tidy-cleaned.csv'), na_filter=False)
        passp = clean(df[df.Passport_ISO2 == passport.upper()].dropna())
        return passp
    except Exception as e:
        print(e)
        return str(e)


if __name__ == '__main__':
    app.run(debug=True)