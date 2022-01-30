from flask import Flask, request, render_template
from datetime import date

from mj_logic import days_from_now_logic, week_dates_logic, calendar_holiday


import holidays

app = Flask(__name__)


today = str(date.today())
TODAY_int = date.today().year
YEARS = [str(i) for i in range(TODAY_int, TODAY_int + 6)]

COUNTRIES = {"Angola": holidays.AO(),
             "Argentina": holidays.AR(),
             "Aruba": holidays.AW(),
             "Australia": holidays.AU(),
             "Austria": holidays.AT(),
             "Azerbaijan": holidays.AZ(),
             "Bangladesh": holidays.BD(),
             "Belarus": holidays.BY(),
             "Belgium": holidays.BE(),
             "Botswana": holidays.BW(),
             "Brazil": holidays.BR(),
             "Bulgaria": holidays.BG(),
             "Burundi": holidays.BI(),
             "Canada": holidays.CA(),
             "Chile": holidays.CL(),
             "China": holidays.CN(),
             "Colombia": holidays.CO(),
             "Croatia": holidays.HR(),
             "Curacao": holidays.CW(),
             "Czechia": holidays.CZ(),
             "Denmark": holidays.DK(),
             "Djibouti": holidays.DJ(),
             "DominicanRepublic": holidays.DO(),
             "Egypt": holidays.EG(),
             "Estonia": holidays.EE(),
             "Ethiopia": holidays.ET(),
             "EuropeanCentralBank": holidays.ECB(),
             "Finland": holidays.FI(),
             "France": holidays.FR(),
             "Georgia": holidays.GE(),
             "Germany": holidays.DE(),
             "Greece": holidays.GR(),
             "Honduras": holidays.HN(),
             "HongKong": holidays.HK(),
             "Hungary": holidays.HU(),
             "Iceland": holidays.IS(),
             "India": holidays.IN(),
             "Ireland": holidays.IE(),
             "Israel": holidays.IL(),
             "Italy": holidays.IT(),
             "Jamaica": holidays.JM(),
             "Japan": holidays.JP(),
             "Kazakhstan": holidays.KZ(),
             "Kenya": holidays.KE(),
             "Korea": holidays.KR(),
             "Latvia": holidays.LV(),
             "Lesotho": holidays.LS(),
             "Lithuania": holidays.LT(),
             "Luxembourg": holidays.LU(),
             "Malaysia": holidays.MY(),
             "Malawi": holidays.MW(),
             "Mexico": holidays.MX(),
             "Morocco": holidays.MA(),
             "Mozambique": holidays.MZ(),
             "Netherlands": holidays.NL(),
             "Namibia": holidays.NA(),
             "NewZealand": holidays.NZ(),
             "Nicaragua": holidays.NI(),
             "Nigeria": holidays.NG(),
             "NorthMacedonia": holidays.MK(),
             "Norway": holidays.NO(),
             "Paraguay": holidays.PY(),
             "Peru": holidays.PE(),
             "Poland": holidays.PL(),
             "Portugal": holidays.PT(),
             "PortugalExt": holidays.PTE(),
             "Romania": holidays.RO(),
             "Russia": holidays.RU(),
             "SaudiArabia": holidays.SA(),
             "Serbia": holidays.RS(),
             "Singapore": holidays.SG(),
             "Slovakia": holidays.SK(),
             "Slovenia": holidays.SI(),
             "SouthAfrica": holidays.ZA(),
             "Spain": holidays.ES(),
             "Swaziland": holidays.SZ(),
             "Sweden": holidays.SE(),
             "Switzerland": holidays.CH(),
             "Taiwan": holidays.TW(),
             "Turkey": holidays.TR(),
             "Tunisia": holidays.TN(),
             "Ukraine": holidays.UA(),
             "UnitedArabEmirates": holidays.AE(),
             "UnitedKingdom": holidays.UK(),
             "UnitedStates": holidays.US(),
             "Venezuela": holidays.VE(),
             "Vietnam": holidays.VN(),
             "Zambia": holidays.ZM(),
             "Zimbabwe": holidays.ZW(),
             }


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/days_from_now", methods=['GET', 'POST'])
def days_from_now():
    global today
    name = ""
    today_str_txt = today
    today_str = today
    if request.method == "POST" and "input_date" in request.form:
        name = request.form.get("input_date")
        name = days_from_now_logic(name)
        today_str = request.form.get("input_date")
    return render_template("days_from_now.html",
                           name=name,
                           today_str=today_str,
                           today_str_txt=today_str_txt)


@app.route("/week_dates", methods=['GET', 'POST'])
def week_dates():
    global today
    today_str = today
    date_1 = ""
    date_Year = ""
    date_Week = ""
    date_2 = ""
    if (request.method == "POST" and "input_Year" in request.form
       and "input_Week" in request.form):
        date_Year = request.form.get("input_Year")
        date_Week = request.form.get("input_Week")
        date_1 = week_dates_logic(date_Year, date_Week)[0]
        date_2 = week_dates_logic(date_Year, date_Week)[1]

    return render_template("week_dates.html",
                           today_str=today_str,
                           date_1=date_1,
                           date_2=date_2)


@app.route("/holiday_planner", methods=['GET', 'POST'])
def holiday_planner():
    z_cal = ''
    CHOOSEN_COUNTRY = ''
    CHOOSEN_YEAR = ''
    if (request.method == "POST" and request.form.get("input_vacation")
       and request.form.get("country") in COUNTRIES
       and request.form.get("year") in YEARS):
        z_cal = (calendar_holiday(int(request.form.get("year")),
                 country=COUNTRIES[request.form.get("country")]))
        CHOOSEN_COUNTRY = request.form.get("country")
        CHOOSEN_YEAR = request.form.get("year")
    return render_template("holiday_planner.html",
                           value1=z_cal,
                           countries=COUNTRIES,
                           years=YEARS,
                           choosen_country=CHOOSEN_COUNTRY,
                           choosen_year=CHOOSEN_YEAR)


@app.route("/what_date", methods=['GET', 'POST'])
def what_date():
    return render_template("what_date.html")
