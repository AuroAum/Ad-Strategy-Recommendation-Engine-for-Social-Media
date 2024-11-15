# app/routes.py

from flask import Blueprint, render_template, request
from app.models import AdStrategy
from app import create_app  # Import the app

# Define the Blueprint for main routes
main = Blueprint('main', __name__)

@main.route('/')
def home():
    # Render the homepage with the form to input ad criteria
    return render_template('home.html')

@main.route('/submit', methods=['POST'])
def submit():
    # Retrieve form data from the POST request
    product_type = request.form.get('product_type')
    age_group = request.form.get('age_group')
    budget = request.form.get('budget')
    # Debug prints
    print(f"Product Type: {product_type}")
    print(f"Age Group: {age_group}")
    print(f"Budget: {budget}")
    # Query the database for matching ad strategies
    recommendations = AdStrategy.query.filter_by(
        product_type=product_type,
        target_age_group=age_group,
        budget_level=budget
    ).all()
    # If no recommendations found, provide a fallback recommendation
    if not recommendations:
        recommendations = AdStrategy.query.filter_by(
            product_type=product_type
        ).all() or AdStrategy.query.filter_by(
            target_age_group=age_group
        ).all() or AdStrategy.query.filter_by(
            budget_level=budget
        ).all() or AdStrategy.query.all()
    # Debug print
    print(f"Recommendations: {recommendations}")
    # Render the results page with the recommendations
    return render_template('results.html', recommendations=recommendations)
