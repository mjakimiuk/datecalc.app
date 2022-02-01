from flask import Flask, request, render_template
from datetime import date
import holidays

from app_functions import (days_from_now_logic,
                           week_dates_logic, calendar_holiday)


app = Flask(__name__)


today = str(date.today())
TODAY_int = date.today().year
YEARS = [str(i) for i in range(TODAY_int, TODAY_int + 6)]

COUNTRIES = {"Angola": getattr(holidays, 'AO'),
             "Argentina": getattr(holidays, 'AR'),
             "Aruba": getattr(holidays, 'AW'),
             "Australia": getattr(holidays, 'AU'),
             "Austria": getattr(holidays, 'AT'),
             "Azerbaijan": getattr(holidays, 'AZ'),
             "Bangladesh": getattr(holidays, 'BD'),
             "Belarus": getattr(holidays, 'BY'),
             "Belgium": getattr(holidays, 'BE'),
             "Botswana": getattr(holidays, 'BW'),
             "Brazil": getattr(holidays, 'BR'),
             "Bulgaria": getattr(holidays, 'BG'),
             "Burundi": getattr(holidays, 'BI'),
             "Canada": getattr(holidays, 'CA'),
             "Chile": getattr(holidays, 'CL'),
             "China": getattr(holidays, 'CN'),
             "Colombia": getattr(holidays, 'CO'),
             "Croatia": getattr(holidays, 'HR'),
             "Curacao": getattr(holidays, 'CW'),
             "Czechia": getattr(holidays, 'CZ'),
             "Denmark": getattr(holidays, 'DK'),
             "Djibouti": getattr(holidays, 'DJ'),
             "DominicanRepublic": getattr(holidays, 'DO'),
             "Egypt": getattr(holidays, 'EG'),
             "Estonia": getattr(holidays, 'EE'),
             "Ethiopia": getattr(holidays, 'ET'),
             "EuropeanCentralBank": getattr(holidays, 'ECB'),
             "Finland": getattr(holidays, 'FI'),
             "France": getattr(holidays, 'FR'),
             "Georgia": getattr(holidays, 'GE'),
             "Germany": getattr(holidays, 'DE'),
             "Greece": getattr(holidays, 'GR'),
             "Honduras": getattr(holidays, 'HN'),
             "HongKong": getattr(holidays, 'HK'),
             "Hungary": getattr(holidays, 'HU'),
             "Iceland": getattr(holidays, 'IS'),
             "India": getattr(holidays, 'IN'),
             "Ireland": getattr(holidays, 'IE'),
             "Israel": getattr(holidays, 'IL'),
             "Italy": getattr(holidays, 'IT'),
             "Jamaica": getattr(holidays, 'JM'),
             "Japan": getattr(holidays, 'JP'),
             "Kazakhstan": getattr(holidays, 'KZ'),
             "Kenya": getattr(holidays, 'KE'),
             "Korea": getattr(holidays, 'KR'),
             "Latvia": getattr(holidays, 'LV'),
             "Lesotho": getattr(holidays, 'LS'),
             "Lithuania": getattr(holidays, 'LT'),
             "Luxembourg": getattr(holidays, 'LU'),
             "Malaysia": getattr(holidays, 'MY'),
             "Malawi": getattr(holidays, 'MW'),
             "Mexico": getattr(holidays, 'MX'),
             "Morocco": getattr(holidays, 'MA'),
             "Mozambique": getattr(holidays, 'MZ'),
             "Netherlands": getattr(holidays, 'NL'),
             "Namibia": getattr(holidays, 'NA'),
             "NewZealand": getattr(holidays, 'NZ'),
             "Nicaragua": getattr(holidays, 'NI'),
             "Nigeria": getattr(holidays, 'NG'),
             "NorthMacedonia": getattr(holidays, 'MK'),
             "Norway": getattr(holidays, 'NO'),
             "Paraguay": getattr(holidays, 'PY'),
             "Peru": getattr(holidays, 'PE'),
             "Poland": getattr(holidays, 'PL'),
             "Portugal": getattr(holidays, 'PT'),
             "PortugalExt": getattr(holidays, 'PTE'),
             "Romania": getattr(holidays, 'RO'),
             "Russia": getattr(holidays, 'RU'),
             "SaudiArabia": getattr(holidays, 'SA'),
             "Serbia": getattr(holidays, 'RS'),
             "Singapore": getattr(holidays, 'SG'),
             "Slovakia": getattr(holidays, 'SK'),
             "Slovenia": getattr(holidays, 'SI'),
             "SouthAfrica": getattr(holidays, 'ZA'),
             "Spain": getattr(holidays, 'ES'),
             "Swaziland": getattr(holidays, 'SZ'),
             "Sweden": getattr(holidays, 'SE'),
             "Switzerland": getattr(holidays, 'CH'),
             "Taiwan": getattr(holidays, 'TW'),
             "Turkey": getattr(holidays, 'TR'),
             "Tunisia": getattr(holidays, 'TN'),
             "Ukraine": getattr(holidays, 'UA'),
             "UnitedArabEmirates": getattr(holidays, 'AE'),
             "UnitedKingdom": getattr(holidays, 'UK'),
             "UnitedStates": getattr(holidays, 'US'),
             "Venezuela": getattr(holidays, 'VE'),
             "Vietnam": getattr(holidays, 'VN'),
             "Zambia": getattr(holidays, 'ZM'),
             "Zimbabwe": getattr(holidays, 'ZW'),
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
    generated_list = ''
    choosen_country_flask = ''
    choosen_year_flask = ''
    holiday_list_flask = ''
    if (request.method == "POST" and request.form.get("input_vacation")
       and request.form.get("country") in COUNTRIES
       and request.form.get("year") in YEARS):
        generated_list = (calendar_holiday(int(request.form.get("year")),
                                           country=COUNTRIES[
                                           request.form.get("country")]()))
        choosen_country_flask = request.form.get("country")
        choosen_year_flask = request.form.get("year")
        holiday_list_flask = [(f"{date.day}-{date.strftime('%B')} - {name}")
                              for date, name in
                              sorted(COUNTRIES[request.form.get("country")]
                              (years=int(choosen_year_flask)).items())]
    return render_template("holiday_planner.html",
                           generated_list_jinja=generated_list,
                           countries_jinja=COUNTRIES,
                           years_jinja=YEARS,
                           choosen_country_jinja=choosen_country_flask,
                           choosen_year_jinja=choosen_year_flask,
                           holiday_list_jinja=holiday_list_flask)


@app.route("/what_date", methods=['GET', 'POST'])
def what_date():
    return render_template("what_date.html")
