from flask import Flask, render_template, flash, redirect, url_for, request
from flask_bootstrap import Bootstrap
from forms import StepOneForm
app = Flask(__name__)
app.secret_key = 'lkgknwlkknflkewfnokwek'

bootstrap = Bootstrap()
bootstrap.init_app(app)

# route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def step1():
    form = StepOneForm()
    if request.method == 'POST' and form.validate():
        # TODO: update values in gspread
        return redirect(url_for('step2'))
    return render_template('step1.html', form = form)

# route for handling the login page logic
@app.route('/step2', methods=['GET', 'POST'])
def step2():
    form = StepTwoForm()
    if request.method == 'POST' and form.validate():
        # TODO: update values in gspread
        return redirect(url_for('step3'))
    return render_template('step2.html', form=form)

# route for handling the login page logic
@app.route('/step3', methods=['GET', 'POST'])
def step3():
    form = StepThreeForm()
    if request.method == 'POST' and form.validate():
        # TODO: update values in gspread
        return redirect(url_for('step4'))
    return render_template('step3.html', form=form)

# route for handling the login page logic
@app.route('/step4', methods=['GET', 'POST'])
def step4():
    form = StepFourForm()
    if request.method == 'POST' and form.validate():
        # TODO: update values in gspread
        return redirect(url_for('final'))
    return render_template('step4.html', form=form)

# route for handling the login page logic
@app.route('/final', methods=['GET', 'POST'])
def final():
    return render_template('step5.html')

if __name__ == "__main__":
    app.run()
