from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email

class CourseForm(FlaskForm):
    title = StringField('Course Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Add Course')

class EnrollForm(FlaskForm):
    name = StringField('Your Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Enroll')

