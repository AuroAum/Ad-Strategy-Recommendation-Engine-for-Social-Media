from app import create_app, db
from app.models import UserData, AdStrategy

app = create_app()

with app.app_context():
    # Drop all tables and recreate them
    db.drop_all()
    db.create_all()

    # Sample data for UserData
    user_data_samples = [
        UserData(age_group="18-24", income_bracket="low", attention_span=120.5, interests="technology,gaming"),
        UserData(age_group="25-34", income_bracket="medium", attention_span=200.0, interests="fitness,health"),
        UserData(age_group="35-44", income_bracket="high", attention_span=150.5, interests="fashion,travel"),
        UserData(age_group="45-54", income_bracket="low", attention_span=100.0, interests="news,sports"),
        UserData(age_group="18-24", income_bracket="high", attention_span=300.0, interests="gaming,movies"),
        # Additional sample data
        UserData(age_group="55-64", income_bracket="medium", attention_span=180.0, interests="gardening,cooking"),
        UserData(age_group="65+", income_bracket="low", attention_span=90.0, interests="reading,walking"),
        UserData(age_group="25-34", income_bracket="high", attention_span=250.0, interests="technology,travel"),
        UserData(age_group="35-44", income_bracket="medium", attention_span=130.0, interests="fitness,news"),
        UserData(age_group="45-54", income_bracket="high", attention_span=110.0, interests="fashion,health"),
    ]

    # Sample data for AdStrategy
    ad_strategy_samples = [
        AdStrategy(product_type="Electronics", target_age_group="18-24", budget_level="Low", recommended_platform="Instagram", content_category="Video", description="Target young adults with engaging video content on Instagram."),
        AdStrategy(product_type="Electronics", target_age_group="18-24", budget_level="Medium", recommended_platform="Instagram", content_category="Video", description="Increase budget for higher quality video content on Instagram."),
        AdStrategy(product_type="Electronics", target_age_group="18-24", budget_level="High", recommended_platform="Instagram", content_category="Video", description="Maximize reach with premium video content on Instagram."),
        AdStrategy(product_type="Electronics", target_age_group="25-34", budget_level="Low", recommended_platform="Facebook", content_category="Story", description="Use Facebook Stories to reach young professionals."),
        AdStrategy(product_type="Electronics", target_age_group="25-34", budget_level="Medium", recommended_platform="Facebook", content_category="Story", description="Enhance Facebook Stories with interactive elements."),
        AdStrategy(product_type="Electronics", target_age_group="25-34", budget_level="High", recommended_platform="Facebook", content_category="Story", description="Invest in high-quality Facebook Stories for maximum engagement."),
        AdStrategy(product_type="Electronics", target_age_group="35-44", budget_level="Low", recommended_platform="Twitter", content_category="Image", description="Share engaging images on Twitter to attract middle-aged adults."),
        # Additional sample data with new platforms and descriptions
        AdStrategy(product_type="Fashion", target_age_group="18-24", budget_level="Low", recommended_platform="Instagram", content_category="Image", description="Showcase fashion products with attractive images on Instagram."),
        AdStrategy(product_type="Fashion", target_age_group="25-34", budget_level="Medium", recommended_platform="Pinterest", content_category="Image", description="Use Pinterest to share fashion inspiration with high-quality images."),
        AdStrategy(product_type="Fashion", target_age_group="35-44", budget_level="High", recommended_platform="Facebook", content_category="Video", description="Create engaging fashion videos for Facebook."),
        AdStrategy(product_type="Health", target_age_group="45-54", budget_level="Low", recommended_platform="Twitter", content_category="Article", description="Share health articles on Twitter to inform and engage."),
        AdStrategy(product_type="Health", target_age_group="55-64", budget_level="Medium", recommended_platform="Facebook", content_category="Video", description="Use Facebook videos to share health tips and advice."),
        AdStrategy(product_type="Health", target_age_group="65+", budget_level="High", recommended_platform="Instagram", content_category="Story", description="Engage older adults with Instagram Stories focused on health."),
        AdStrategy(product_type="Technology", target_age_group="18-24", budget_level="Low", recommended_platform="YouTube", content_category="Video", description="Create tech review videos for YouTube to attract young tech enthusiasts."),
        AdStrategy(product_type="Technology", target_age_group="25-34", budget_level="Medium", recommended_platform="LinkedIn", content_category="Article", description="Share in-depth tech articles on LinkedIn for professionals."),
        AdStrategy(product_type="Technology", target_age_group="35-44", budget_level="High", recommended_platform="Twitter", content_category="Image", description="Use Twitter to share tech news and updates with engaging images."),
        AdStrategy(product_type="Entertainment", target_age_group="18-24", budget_level="Low", recommended_platform="TikTok", content_category="Video", description="Create short, engaging videos on TikTok for young audiences."),
        AdStrategy(product_type="Entertainment", target_age_group="25-34", budget_level="Medium", recommended_platform="YouTube", content_category="Video", description="Produce high-quality entertainment videos for YouTube."),
        AdStrategy(product_type="Entertainment", target_age_group="35-44", budget_level="High", recommended_platform="Facebook", content_category="Video", description="Invest in premium entertainment videos for Facebook."),
    ]

    # Add sample data to the database
    db.session.bulk_save_objects(user_data_samples)
    db.session.bulk_save_objects(ad_strategy_samples)
    db.session.commit()