from app import db

class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age_group = db.Column(db.String(20), nullable=False)
    income_bracket = db.Column(db.String(20), nullable=False)
    attention_span = db.Column(db.Float, nullable=False)
    interests = db.Column(db.String(200), nullable=False)

class AdStrategy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_type = db.Column(db.String(50), nullable=False)
    target_age_group = db.Column(db.String(20), nullable=False)
    budget_level = db.Column(db.String(20), nullable=False)
    recommended_platform = db.Column(db.String(50), nullable=False)
    content_category = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(500), nullable=True)  # Add this line
