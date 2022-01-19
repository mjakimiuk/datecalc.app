from flask import Flask, request, render_template
import mj_logic
from datetime import datetime, date

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/date_from_now", methods=['GET','POST'])
def date_from_now():
    name = ""
    t_delta = ""
    if request.method == "POST" and "input_date" in request.form:
        name = request.form.get("input_date")
        dt = datetime.strptime(name, "%d/%m/%Y")
        today = datetime.combine(date.today(), datetime.min.time())
        t_delta = str((dt-today).days)
    return render_template("date_from_now.html",
                            name = t_delta)


@app.route("/week_dates")
def week_dates():
    return render_template("week_dates.html")


@app.route("/holiday_planner")
def holiday_planner():
    return render_template("holiday_planner.html")