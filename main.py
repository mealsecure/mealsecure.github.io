from flask import Flask, request, url_for, redirect, render_template
from script import mainFunction

app = Flask(__name__)

""""@app.route("/")
def index():
    return render_template("index.html")"""

@app.route("/", methods=["GET"])
def submit():
    censusTractCode = request.args.get("census-tract-code", None)
    state = request.args.get("state", None)
    county = request.args.get("county", None)
    listValues = mainFunction(censusTractCode, county, state)
    myhtml = "<head><link rel='stylesheet' type='text/css' title='regular' href='styles.css' /></head><br><br><label style='font-size: 2em; font-family: Georgia, 'Times New Roman', Times, serif;'><span style='box-sizing: content box; width: 100%; border: solid #5B6DCD 10px;'><h1>{}, {} of population {}</h1><h1>{}% of its residents are just low-income</h1><h1>{}% of its residents are low-income and low-access</label></form></span><p style='font-size: 30px; padding: 3px;'>Food insecurity is defined by the USDA as 'a lack of consistent access to enough food for an active, healthy lifestyle.' All households are vulnerable to food insecurity - it's not solely based on income level. Many factors can come into play, including lack of affordable housing, health problems, prohibitively high medical costs, and low wages.</p><p>USDA defines 'low-income and low access' as a tract with at least 500 people, or a third of the population, living more than 1 mile in urban areas or 10 miles in rural areas from the nearest supermarket or large grocery store. Since your tract has a LILA percentage of {}, your tract is flagged for low-income and low access when considering low accessibilty at 1 and 10 miles.</p>".format(county, state, listValues[0], listValues[3], listValues[2], listValues[2])
    return myhtml

app.run(debug=True, host="0.0.0.0", port=5555)

"""return '''
        <h1>{}, {} of population {}</h1>
        <h1>{} of its residents are just low-income.</h1>
        <h1>{} of its residents are low-income and low-access.'''.format(county, state, listValues[0], listValues[3], listValues[2])
        
            myhtml = "<head><link rel='stylesheet' type='text/css' title='regular' href='styles.css' /></head><form method='get' id='dataForm' style='text-align: center;'><input type='text' name='state' id='state' style='width: 20vw; height: 6vh; padding: 3px; font-size: 2em; margin: 2px;' /><input type='submit' id='submitButton' style='cursor: pointer; padding: 5px; font-size: 1.2em;' /><br><br><label style='font-size: 2em; font-family: Georgia, 'Times New Roman', Times, serif;'>" + state + "</label></form>"
    return myhtml"""