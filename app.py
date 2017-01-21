from flask import Flask, render_template, flash, redirect, url_for, request
from flask_bootstrap import Bootstrap
from forms import StepOneForm
from gsheets import googleSheet
import json

app = Flask(__name__)
app.secret_key = 'lkgknwlkknflkewfnokwek'
GSHEET_KEY = '12UCWPoJ46pMkE5DGZJiy303xQ1GYUGyHB8R5uf6TuPM'

bootstrap = Bootstrap()
bootstrap.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def step1():
    form = StepOneForm()
    if request.method == 'POST' and form.validate():
        # TODO: update values in gspread
        return redirect(url_for('step2'))
    return render_template('step1.html', form = form)

@app.route('/step2', methods=['GET', 'POST'])
def step2():
    form = StepTwoForm()
    if request.method == 'POST' and form.validate():
        # TODO: update values in gspread
        return redirect(url_for('step3'))
    return render_template('step2.html', form=form)

@app.route('/step3', methods=['GET', 'POST'])
def step3():
    form = StepThreeForm()
    if request.method == 'POST' and form.validate():
        # TODO: update values in gspread
        return redirect(url_for('step4'))
    return render_template('step3.html', form=form)

@app.route('/step4', methods=['GET', 'POST'])
def step4():
    form = StepFourForm()
    if request.method == 'POST' and form.validate():
        # TODO: update values in gspread
        return redirect(url_for('final'))
    return render_template('step4.html', form=form)

@app.route('/final', methods=['GET', 'POST'])
def final():
    return render_template('step5.html')

@app.route('/chart_data', methods=['GET', 'POST'])
def get_chart_data():
    data = googleSheet(GSHEET_KEY).get_chart_data()
    title = data[0]

    output = []
    for row in data[1:]:
        d = {}
        for i in range(len(title)):
            d[title[i]] = float(row[i].replace("$", "").replace(",", ""))
        output.append(d)

    return json.dumps(output)


if __name__ == "__main__":
    app.run()
