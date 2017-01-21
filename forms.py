from wtforms import SubmitField, SelectField, StringField, IntegerField, TextAreaField
from wtforms.validators import Required, NumberRange, Length
from wtforms_components import DateField, TimeField
from flask_wtf import FlaskForm

class StepOneForm(FlaskForm):
    age = IntegerField('Age', validators=[NumberRange(min=20, max=90, 
        message="Please enter an age between 20 and 90."), Required()])
    salary = IntegerField('Current Salary', validators=[NumberRange(min=0, 
        message="Please enter a salary of at least 0."), Required()])
    savings = IntegerField('Current Savings', validators=[NumberRange(min=0, 
        message="How much have you saved up? Don't enter negative numbers; we'll ask you about loans later."), Required()])
    perc_saved = IntegerField('% of Salary Saved', validators=[NumberRange(min=0, max=100,
        message="Please enter a number between 0 and 100."), Required()])
    submit       = SubmitField()


class StepTwoForm(FlaskForm):
    age = IntegerField('Age', validators=[NumberRange(min=20, max=90, 
        message="Please enter an age between 20 and 90."), Required()])
    salary = IntegerField('Current Salary', validators=[NumberRange(min=0, 
        message="Please enter a salary of at least 0."), Required()])
    savings = IntegerField('Current Savings', validators=[NumberRange(min=0, 
        message="How much have you saved up? Don't enter negative numbers; we'll ask you about loans later."), Required()])
    perc_saved = IntegerField('% of Salary Saved', validators=[NumberRange(min=0, max=100,
        message="Please enter a number between 0 and 100."), Required()])
    submit       = SubmitField()


class StepThreeForm(FlaskForm):
    age = IntegerField('Age', validators=[NumberRange(min=20, max=90, 
        message="Please enter an age between 20 and 90."), Required()])
    salary = IntegerField('Current Salary', validators=[NumberRange(min=0, 
        message="Please enter a salary of at least 0."), Required()])
    savings = IntegerField('Current Savings', validators=[NumberRange(min=0, 
        message="How much have you saved up? Don't enter negative numbers; we'll ask you about loans later."), Required()])
    perc_saved = IntegerField('% of Salary Saved', validators=[NumberRange(min=0, max=100,
        message="Please enter a number between 0 and 100."), Required()])
    submit       = SubmitField()


class StepFourForm(FlaskForm):
    age = IntegerField('Age', validators=[NumberRange(min=20, max=90, 
        message="Please enter an age between 20 and 90."), Required()])
    salary = IntegerField('Current Salary', validators=[NumberRange(min=0, 
        message="Please enter a salary of at least 0."), Required()])
    savings = IntegerField('Current Savings', validators=[NumberRange(min=0, 
        message="How much have you saved up? Don't enter negative numbers; we'll ask you about loans later."), Required()])
    perc_saved = IntegerField('% of Salary Saved', validators=[NumberRange(min=0, max=100,
        message="Please enter a number between 0 and 100."), Required()])
    submit       = SubmitField()
