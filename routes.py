from flask import Blueprint, render_template, redirect, url_for, request
from app import db
from models import Course, Enrollment
from forms import CourseForm, EnrollForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    courses = Course.query.all()
    return render_template('index.html', courses=courses)

@main.route('/add', methods=['GET', 'POST'])
def add_course():
    form = CourseForm()
    if form.validate_on_submit():
        new_course = Course(title=form.title.data, description=form.description.data)
        db.session.add(new_course)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('add_course.html', form=form)

@main.route('/enroll/<int:course_id>', methods=['GET', 'POST'])
def enroll(course_id):
    course = Course.query.get_or_404(course_id)
    form = EnrollForm()
    if form.validate_on_submit():
        enrollment = Enrollment(name=form.name.data, email=form.email.data, course_id=course.id)
        db.session.add(enrollment)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('enroll.html', course=course, form=form)

