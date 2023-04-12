from flask import Blueprint, jsonify, render_template, request, redirect, url_for
from helpers import token_required
from models import db, User, Car, car_schema, cars_schema
from flask_login import login_required, current_user

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@site.route('/cars')
@login_required
def cars():
    cars = Car.query.filter_by(user_token=current_user.token).all()
    return render_template('cars.html', cars=cars)
