from flask import Flask, request, url_for, redirect, render_template

app = Flask(__name__)
@app.route("/results")
def results():
    return render_template('results.html')

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        censusTractCode = request.args.get("census-tract-code", None)
        state = request.args.get("state", None)
        county = request.args.get("county", None)
        return '''
            <h1>{}, {}</h1>
            <h1>{} of its residents are just low-income.</h1>
            <h1>{} of its residents are low-income and low-access.'''.format(county, state, county, state)
    return '''
        <form method="POST>
            <div><label>Census Tract Code: <input type="number" name="census-tract-code"></label>
            <div><label>County: <input type="text" name="county"></label>
            <div><label>State: <input type="text" name="state"></label>
            <input type="submit" value="Search">
        </form>
    '''

def invalidation():
    return False

app.run(debug=True, host="0.0.0.0", port=80)