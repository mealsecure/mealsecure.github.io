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
    myhtml = "<head><link rel='stylesheet' type='text/css' title='regular' href='styles.css' /></head><form method='get' id='dataForm' style='text-align: center;'><input type='text' name='state' id='state' style='width: 20vw; height: 6vh; padding: 3px; font-size: 2em; margin: 2px;' /><input type='submit' id='submitButton' style='cursor: pointer; padding: 5px; font-size: 1.2em;' /><br><br><label style='font-size: 2em; font-family: Georgia, 'Times New Roman', Times, serif;'><h1>'{}, {} of population {}'.format(county, state, listValues[0])</h1><h1>'{} of its residents are just low-income.'.format(listValues[3])</h1><h1>'{} of its residents are low-income and low-access'.format(listValues[2])</label></form>"
    return myhtml

app.run(debug=True, host="0.0.0.0", port=5555)

"""return '''
        <h1>{}, {} of population {}</h1>
        <h1>{} of its residents are just low-income.</h1>
        <h1>{} of its residents are low-income and low-access.'''.format(county, state, listValues[0], listValues[3], listValues[2])
        
            myhtml = "<head><link rel='stylesheet' type='text/css' title='regular' href='styles.css' /></head><form method='get' id='dataForm' style='text-align: center;'><input type='text' name='state' id='state' style='width: 20vw; height: 6vh; padding: 3px; font-size: 2em; margin: 2px;' /><input type='submit' id='submitButton' style='cursor: pointer; padding: 5px; font-size: 1.2em;' /><br><br><label style='font-size: 2em; font-family: Georgia, 'Times New Roman', Times, serif;'>" + state + "</label></form>"
    return myhtml"""